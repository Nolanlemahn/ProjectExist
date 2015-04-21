init -1 python:

    def size_reset():
        renpy.reset_physical_size()
    config.start_callbacks.append(size_reset)

    config.python_callbacks = []
    config.interact_callbacks = []

#First, we'll define our persistents
init -1 python hide:
    _preferences.set_volume('music', 0.5)

    if persistent.seen_move is None:
        persistent.seen_move = [""]
        for x in range(0, 10001):
            persistent.seen_move.append("")
        persistent.seen_move[10001] = "not_none"
        
    if persistent.choice_rollback is None:
        persistent.choice_rollback = False
    if persistent.all_rollback is None:
        persistent.all_rollback = False
    if persistent.debugmenu_seen is None:
        persistent.debugmenu_seen = False
    if persistent.debugmenu_installed is None:
        persistent.debugmenu_installed = False
    if persistent.imabetatester_seen is None:
        persistent.imabetatester_seen = False
    if persistent.imabetatester is None:
        persistent.imabetatester = False
        
    if persistent.dlc1_installed is None:
        persistent.dlc1_installed = False

    if persistent.seen_natalie is None:
        persistent.seen_natalie = False
    if persistent.seen_tamara is None:
        persistent.seen_tamara = False
    if persistent.seen_lilian is None:
        persistent.seen_lilian = False
    if persistent.seen_athena is None:
        persistent.seen_athena = False
    if persistent.seen_masamune is None:
        persistent.seen_masamune = False
    if persistent.seen_ultraman is None:
        persistent.seen_ultraman = False
    if persistent.seen_wil is None:
        persistent.seen_wil = False
    config.default_fullscreen = False
    ## The default text speed in characters per second. 0 is infinite.
    config.default_text_cps = 20
    config.fix_rollback_without_choice = False

# Temporary.
screen _trace_screen:

    zorder 1501

    if _console.traced_expressions:

        frame style "_console_trace":

            vbox:

                for expr in _console.traced_expressions:
                    python:
                        try:
                            value = repr(eval(expr))
                        except:
                            value = "eval failed"

                    hbox:
                        #text "[expr!q]: " style "_console_trace_var"
                        text "[value!q]" style "_console_trace_value"

init -2 python:
    def show_rwatch():
        style._console_trace_value = style.alert_text
        renpy.watch(get_watch(1))#,
                     #xpos=1.0, xanchor='right', 
                     #ypos=0.15, yanchor='top')
        #if renpy.config.developer:
        renpy.watch(get_watch(2))#,  
                    #xpos=1.0, xanchor='right',
                    #ypos=0.2, yanchor='top')
        #renpy.show_screen("_trace_screen")
    config.start_callbacks.append(show_rwatch)

    def get_watch(index):
        if index is 1:
            return "renpy.get_filename_line()"
        elif index is 2:
            return "\"Mouse was at: \" + (', '.join(str(x) for x in renpy.get_mouse_pos()))"
        else:
            return "\"\""

#init -2:
    #$ _console_trace_value = style.alert_text
    #$ show_rwatch()

#These are our styles and whatnot
init -1:
    $ in_debug = False
    $ in_menu = False
    
    transform slide_down:
        xalign 0.5 yalign 0.0
        linear 4.0 yalign 0.3
    
    #[Reserved for stat menu checks
    #$ right_after_question = False
    $ notin_other_stats = True
    $ inventory_see = True
    $ main_char_show_rpg = False
    $ enemy_char_show_rpg = False
    $ single_death_check = False
    $ single_combat_check = False
    $ battle_mode = False
    $ ingame = False
    $ battle_mode = False
    $ has_phone = False
    #]
    
    $ main_status = "None"
    $ enemy_status = "None"
    $ user_adjustment = ui.adjustment()

    $ tooltiptext = "test"
    $ tooltipped = False

    $ walletshow = False
    $ clock = False
    $ ui_check = False
    $ strchange = ""
    $ intchange = 1
    
    $ fight_is_1v1 = False
    $ johnathan_set_up = False
    #[
    $ updateUIroutine = 0
    #]
    
init -2 python:
    import os
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    config.windows_icon = "icon.png"
    config.window_icon = "icon.png"

    ## These values tell Ren'Py how to build a distribution.
    config.version = "v0.2.8_(1066)"
    config.log = os.path.abspath(config.gamedir + "/../debuglog.txt")
    build.directory_name = "ProjEx_" + config.version
    build.executable_name = "Project Exist"
    build.include_update = True
    build.classify('***/Project_Exist*.zip', None)
    build.classify('flowcharts/**', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('cleanup.bat', None)
    build.classify('cleanup.command', None)
    build.classify("**.rpy", None)


    build.documentation('*.html')
    build.documentation('*.txt')
    #build.documentation('*.pdf')

init python:
    adj=user_adjustment