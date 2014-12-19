# readback.rpy
# drop in readback module for Ren'Py by delta
# simplified/updated around Ren'Py version 6.13.12
# this file is licensed under the terms of the WTFPL
# see http://sam.zoy.org/wtfpl/COPYING for details

init -4:
    $ in_countdown = False

init -3 python:

    # Styles.
    style.readback_window.xmaximum = 1000
    style.readback_window.ymaximum = 700
    style.readback_window.align = (.5, .5)

    style.readback_frame.background = None
    style.readback_frame.xpadding = 10
    style.readback_frame.xmargin = 5
    style.readback_frame.ymargin = 5

    style.readback_text.color = "#fff"

    style.create("readback_button", "readback_text")
    style.readback_button.background = None

    style.create("readback_button_text", "readback_text")
    style.readback_button_text.selected_color = "#f12"
    style.readback_button_text.hover_color = "#f12"

    style.readback_label_text.bold = True

    # starts adding new config variables
    config.locked = False

    # Configuration Variable for Text History
    config.readback_buffer_length = 50 # number of lines stored
    config.readback_full = True # completely replaces rollback, False = readback accessible from game menu only (dev mode)
    config.readback_disallowed_tags = ["size"] # a list of tags that will be removed in the text history
    config.readback_choice_prefix = ">> "   # this is prefixed to the choices the user makes in readback
    config.readback_space_after_nvl_clear = True   # optionally add a sort of paragraph break when "nvl clear" is used
    config.readback_nvl_page = False  # Make scrolling use NVL pages rather than "smooth" scrolling
                                     # If you're using this mode, you probably want to adjust
                                     # readback_buffer_length

    # end
    config.locked = True

init -2 python:

    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            super(ReadbackADVCharacter, self).do_done(who, what)
            return

        def do_extend(self):
            delete_last_line()
            super(ReadbackADVCharacter, self).do_extend()
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            super(ReadbackNVLCharacter, self).do_done(who, what)
            return

        def do_extend(self):
            delete_last_line()
            super(ReadbackNVLCharacter, self).do_extend()
            return

    adv = ReadbackADVCharacter()
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter

    # overwriting standard menu handler
    # Overwriting menu functions makes Text History log choice which users choose.
    def menu(items, **add_input):
        rv = renpy.display_menu(items, **add_input)

        # logging menu choice label.
        for label, val in items:
            if rv == val:
                store_say(None, config.readback_choice_prefix + label)
        return rv

    # Overwriting nvl menu function
    builtin_nvl_menu = nvl_menu
    def nvl_menu(items):
        rv = builtin_nvl_menu(items)
        for label, val in items:
            if rv == val:
                store_say(None, config.readback_choice_prefix + label)
        return rv

    builtin_nvl_clear = nvl_clear
    def nvl_clear():
        builtin_nvl_clear()
        if config.readback_nvl_page:
            readback_buffer.append([])
        elif config.readback_space_after_nvl_clear:
            readback_buffer.append((None, ""))

    def readback_reset():
        global readback_buffer
        if config.readback_nvl_page:
            readback_buffer = [ [] ]
        else:
            readback_buffer = [ ]

    config.start_callbacks.append(readback_reset)

    def store_say(who, what):
        global readback_buffer
        new_line = (preparse_say_for_store(who), preparse_say_for_store(what))
        if config.readback_nvl_page:
            readback_buffer[-1].append(new_line)
        else:
            readback_buffer.append(new_line)
        readback_prune()

    def delete_last_line():
        global readback_buffer
        if config.readback_nvl_page:
            del readback_buffer[-1][-1]
        else:
            del readback_buffer[-1]

    # remove text tags from dialogue lines
    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"

    import re
    readback_remove_tags_expr = re.compile(disallowed_tags_regexp) # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global readback_remove_tags_expr
        if input:
            return re.sub(readback_remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]

    # keymap overriding to show text_history.
    def readback_catcher():
        ui.add(renpy.Keymap(rollback=((SetVariable("readback_yvalue", 1.0)), If(not store.in_countdown, true=ShowMenu("text_history"), false=None))))
        ui.add(renpy.Keymap(rollforward=ui.returns(None)))

    if config.readback_full:
        config.rollback_enabled = False
        config.overlay_functions.append(readback_catcher)

init python:
    readback_yvalue = 1.0

    # support routines for scrolling screen

    class ReadbackAdj(ui.adjustment):
        def change(self,value):
            if value > self._range and self._value == self._range:
                return Return()
            else:
                return ui.adjustment.change(self, value)

    def readback_store_yvalue(y):
        global readback_yvalue
        readback_yvalue = int(y)

    # support routines for paged screen

    def readback_change_page(y):
        global readback_yvalue
        readback_yvalue = int(y)
        renpy.restart_interaction()

    def readback_paged_max():
        max = len(readback_buffer) - 1
        if max > 0 and len(readback_buffer[max]) == 0:
            max = max - 1
        return max

    def readback_fix_yvalue():
        global readback_yvalue
        if not isinstance(readback_yvalue, int):
            readback_yvalue = readback_paged_max()

    def readback_show_prev_page():
        global readback_yvalue
        if (readback_yvalue > 0):
            readback_yvalue -= 1
            renpy.restart_interaction()

    def readback_show_next_page():
        global readback_yvalue
        if (readback_yvalue < readback_paged_max()):
            readback_yvalue += 1
            renpy.restart_interaction()
        else:
            return True

# Text History Screen.
screen text_history:
    tag menu
    if config.readback_nvl_page:
        $ readback_fix_yvalue()

        window:
            style_group "readback"

            frame:
                yfill True
                has vbox

                key "rollback" action readback_show_prev_page
                key "rollforward" action readback_show_next_page

                null height 10

                for line in readback_buffer[readback_yvalue]:

                    if line[0]:
                        label line[0]

                    text line[1]

                    null height 10

            textbutton _("Return") action Return() align (.97, 1.0)

    else:
        $ adj = ReadbackAdj(changed = readback_store_yvalue, step = 300)
        window:
            style_group "readback"

            side "c r":

                frame:
                    has viewport:
                        mousewheel True
                        draggable True
                        yinitial readback_yvalue
                        yadjustment adj
                    vbox:
                        null height 10

                        for line in readback_buffer:

                            if line[0]:
                                label line[0]

                            if (line[1] != None):
                                text line[1]

                            null height 10

                bar adjustment adj style 'vscrollbar'

            textbutton _("Return") action Return() align (.97, 1.0)
