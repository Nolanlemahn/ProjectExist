init python:
    #question should be a string or None, *answers is any number of strings as additional parameters
    #selected answer becomes red on-screen, returns integer (min=1) in accordance to which answer chosen
    #additionally requires following definition or similar (ctc need not be defined):
    # $ nvlcap = NVLCharacter(None, kind=nvl, ctc=anim.Blink("extra/arrow.png"))
    def init_points():
        for i in range(0, 10001):
            points.append(0)
        return
        
    def sio_l(called_scene):
        renpy.scene()
        renpy.show("bg blackdrop")
        renpy.show("empty")
        renpy.with_statement(dissolve)
        renpy.scene()
        renpy.show(called_scene)
        renpy.show("empty")
        renpy.with_statement(dissolve)
        return
        
    def sio_s(called_scene):
        renpy.scene()
        renpy.show(called_scene)
        renpy.with_statement(dissolve)
    
    def nvlq(question, *answers):
        full_answer = ""
        menu_answers = []
        string_answers = []
        num_answers = 0
        
        for answer in answers:
            num_answers = num_answers + 1
            menu_answers.append(("> "+answer, num_answers))
            string_answers.append("> "+answer)
            
        if(question == None):
            result = nvl_menu(menu_answers)
        else:
            q = [(question, None)]
            q.extend(menu_answers)
            result = nvl_menu(q)
            
        string_answers[result-1] = "{color=#f00}" + string_answers[result-1] + "{/color}"
        for answer in string_answers:
            full_answer = full_answer + answer + "\n"
        full_answer = full_answer[:-1]
        
        if(question == None):
            renpy.say(nvlcap, full_answer + "{fast}")
        else:
            renpy.say(nvlcap, question + "\n" + full_answer + "{fast}")
        return result

    def nvlans(q_index, result):
        if(q_index == 0):
            q_answers = ["thought_heaven", "thought_hell", "thought_head_neither", "thought_head_empty"]
        else:
            return None
        return q_answers[result - 1]
        
    def menu_callback(mode, old_modes):
        if mode == "say" or mode == "nvl":
            renpy.hide_screen("countdown_tag")
            renpy.fix_rollback()
        if (renpy.in_fixed_rollback()):
            renpy.hide_screen("countdown_tag")
    config.mode_callbacks.append(menu_callback)
    
    def cd_set(start_time, end_time, target_str):
        #don't bother checking store
        store.time = start_time
        store.timer_range = end_time
        store.timer_jump = target_str
        return
        
label sn_label(select_tip):
    $ selected_note = select_tip
    $ snroutine = 3
    show screen side_note
    if (select_tip=="sn demo"):
        show sn demo:
            xpos 1200 ypos 240
            linear 1.0 xpos 800
            
    if (select_tip=="sn gre"):
        show sn gre:
            xpos 1200 ypos 240
            linear 1.0 xpos 800
            
    if (select_tip=="sn siebener"):
        show sn siebener:
            xpos 1200 ypos 240
            linear 1.0 xpos 800
            
    if (select_tip=="sn frank"):
        show sn frank:
            xpos 1200 ypos 240
            linear 1.0 xpos 800
    return

label dev_com(com_dex):
    if(persistent.dev_commentary):
        if(com_dex == 1):
             dev "Developer commentary will look like this. When a reference is deemed necessary, it will appear as a separate button."
        elif(com_dex == "irc"):
             dev "While this IRC server doesn't exist, if it did, Kazuki would be the highest ranked user in this channel. The percent 
                  symbol indicates that he is a half-operator, and can kick/ban any user operator and below."
             dev "Jonathan has voice, the plus. This means that if the channel becomes moderated, he will still be able to talk."
             dev "Wil... Wil has no privileges whatsoever."
        elif(com_dex == "noether"):
             dev "Emmy Noether is best known for her first theorem, which basically states that if an environment has a continuous symmetry, 
                  then there is a corresponding conserved quantity."
             dev "Please see the {a=http://en.wikipedia.org/wiki/Noether%27s_theorem#Informal_statement_of_the_theorem}WikiPedia page{/a} for 
                  more detail. And in the event you didn't get the Lehrer references, please look up Lehrer the Elements, or something 
                  along those lines. You'll thank me afterwards."
        elif(com_dex == "tamaraplus"):
            dev "When I originally wrote this bit, clicking on the tooltip would unlock extra dialogue (and mini-route) in which Kazuki explains 
                 each idiom. This would cause Kazuki to laugh, which would piss Tamara off. Due to tech constraints with the rest of the tooltip 
                 stuff, the idea was scrapped."
    return
