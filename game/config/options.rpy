init -1 python:

    def size_reset():
        try:
            renpy.reset_physical_size()
        except:
            return
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

init -2 python:
    get_watch = [["unused"]]
    get_watch.append("renpy.get_filename_line()")
    get_watch.append("\"Mouse was at: \" + (', '.join(str(x) for x in renpy.get_mouse_pos()))")

    def show_watch():
        #style._console_trace_value = style.alert_text
        watch(get_watch[1], style = style.alert_text, func_name = "script_cursor", 
              xpos=1.0, xanchor='right', ypos=0.15, yanchor='top')
        #if renpy.config.developer:
        watch(get_watch[2], style = style.alert_text, func_name = "mouse_pos",
              xpos=1.0, xanchor='right', ypos=0.2, yanchor='top')
        #renpy.show_screen("_trace_screen")
    config.start_callbacks.append(show_watch)

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

init python:
    adj=user_adjustment