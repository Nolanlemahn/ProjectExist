#######
# File name: doublespeak.rpy
# 
# Description: Allows multiple Characters to speak at once
# 
# Original author: delta, Shiz
# Modifications: Nolan/NintendoToad
# 
# Type: Library, Screen
# 
# Usage:
#     doublespeak Character() Character() String
# --or--
#     doublespeak Character() Character() String String
#######

python early:
    import collections #OrderedDict()

    #####
    # Function name: doublespeak_parse()
    # 
    # Descripiton: Parses a lexer, separating it into parts.
    # 
    # Parameters:
    # lexer - arguments from the renpy statement
    # 
    # Returns: The requested characters and messages as a dict
    #####
    def doublespeak_parse(lexer):
        # We expect the first two expressions to be the characters
        leftchar = lexer.simple_expression()
        rightchar = lexer.simple_expression()
        
        # Take 1 or 2 messages
        leftmsg = eval(lexer.simple_expression())
        if lexer.eol():
            rightmsg = leftmsg
        else:
            rightmsg = eval(lexer.simple_expression())

        # If there are still expressions, break
        if not lexer.eol():
            renpy.error('unexpected leftover data')
            
        # Return the grabbed info
        return { 'chars': [leftchar, rightchar], 'messages': [leftmsg, rightmsg] , 'two_window':[False]}


    #####
    # Function name: doublespeak()
    # 
    # Descripiton: Calls the say Screen with the messages and sayers.
    # 
    # Parameters:
    # info - the Dict() from multispeak_process()
    # 
    # Returns: None
    #####
    def doublespeak(info):
        info = multispeak_process(info)
        longest = sorted(info['messages'], key=len, reverse=True)[0]

        renpy.shown_window()
        renpy.show_screen('say', doublespeak=True, who=info['chars'], what=info['messages'], two_window = info['two_window'])
        
        # Store what is said into readback manually, if it's installed
        if(hasattr(store, "readback_installed")):
            if(store.readback_installed):
                store_say(info['chars'].items()[0][0], info['messages'][0])
                store_say(info['chars'].items()[1][0], info['messages'][1])

        ui.saybehavior(afm=longest)
        result = ui.interact(roll_forward=renpy.roll_forward_info(), type='say')
        renpy.checkpoint(result)

    #####
    # Function name: multispeak_process()
    # 
    # Descripiton: Format the info from doublespeak_parse().
    # 
    # Parameters:
    # info - the Dict() from doublespeak_parse()
    # 
    # Returns: None
    #####
    def multispeak_process(info):
        # Get proper character names.
        chars = collections.OrderedDict()
        for name in info['chars']:
            try:
                char = eval(name)
                
                # Build the prefix, bolding char.name by default
                full_who_prefix = "{b}" + char.who_prefix
                full_who_suffix = char.who_suffix + "{/b}"
                if('color' in char.who_args):
                    full_who_prefix = full_who_prefix + "{color=" + char.who_args["color"] + "}"
                    full_who_suffix = "{/color}" + full_who_suffix
                    
                # Apply prefix/suffix
                if getattr(char, 'dynamic', False):
                    name = full_who_prefix + eval(char.name) + full_who_suffix
                # but don't re-evaluate character names if it isn't dynamic
                else:
                    name = full_who_prefix + char.name + full_who_suffix
                    
                # remove bold tags if style specifies non-bold labels
                if (not style.say_label.bold):
                    name = name[3:-4]
                    
                # apply two_window
                if hasattr(char, 'show_two_window'):
                    renpy.say(None, "wait!")
                    info['two_window'] = getattr(char, 'show_two_window')
                chars[name] = char
            except:
                # If we're rolling back, name may already be how we want it to 
                # be formatted and thus run an exception
                chars[name] = name
        info['chars'] = chars

        # Adjust messages properly.
        messages = []
        for (name, char), message in zip(info['chars'].items(), info['messages']):
            try:
                message = char.what_prefix + message + char.what_suffix
                messages.append(message)
            except:
                # has been transformed or something
                messages.append(message)
        info['messages'] = messages

        return info

    def multispeak_predict(info):
        return []

    def multispeak_lint(info):
        for char in info['chars']:
            try:
                eval(char)
            except:
                # characters that can't be evaluated are not necessarily defined
                renpy.error('unknown character {0}'.format(char))

    def multispeak_next(info):
        return None

    renpy.statements.register('doublespeak', parse=doublespeak_parse, execute=doublespeak, predict=multispeak_predict, lint=multispeak_lint, next=multispeak_next)

