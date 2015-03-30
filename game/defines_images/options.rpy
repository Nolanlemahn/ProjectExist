init -1 python:        
#styles - ui
    style.clipFrame = Style(style.frame)
    style.clipFrame.background = Frame("menus/FoxFrameClip.png", 25, 25)
    
    style.nvl_menu_choice.idle_color = "#ffffffff"
    style.nvl_menu_choice.hover_color = "#ccccccff"
    style.nvl_menu_choice_button.hover_background = "#00000000"
    style.nvl_menu_choice_button.left_margin = 0
    
    style.dev_button = Style(style.button)
    style.dev_button.background = "#FF0000"
    style.dev_button.hover_background = "#FF6600"
    style.dev_button.selected_background = "#000000"
    style.dev_button_text.color = "#000000"
    style.dev_button_text.hover_color = "#000000"
    style.dev_button_text.selected_color = "#000000"
init -1:
    style scentered_text:
        textalign 0.5
        xalign 0.5
        yalign 0.5
        layout "subtitle"
        font "fonts/Respective_Slanted.ttf"
        size 64
    
    
    
    $ cdw_color = (255, 0, 0, 255)#red
    $ style.create("game_box", "frame")
    $ style.game_box.background = Frame("menus/FoxGameBox.png", 25, 25)
    
    $ style.alertnow_text.color = "#FF0000"
    style centered_talker:
        yalign 0.5
        yfill False
        xpadding 10

    #styles - characters; prefix and suffix are explicit colors so readback does colors too
    $ style.create("main_gray", "default")
    $ style.main_gray.color = "#C0C0C0"
    $ char_gray = Character(what_style="main_gray", 
        what_prefix="{color=#C0C0C0}", what_suffix = "{/color}",
        who_prefix="{color=#C0C0C0}", who_suffix = "{/color}")
    $ nvl_gray = Character(what_style="main_gray", kind=nvl,
        what_prefix="{color=#C0C0C0}", what_suffix = "{/color}",
        who_prefix="{color=#C0C0C0}", who_suffix = ":{/color}")
    $ nvl_gray_narr = Character(what_style="main_gray", kind=nvl)

    $ style.create("sub_blue", "default")
    $ style.sub_blue.color = "#ADD8E6"
    $ char_blue = Character(what_style="sub_blue",
        what_prefix="{color=#ADD8E6}", what_suffix = "{/color}",
        who_prefix="{color=#ADD8E6}", who_suffix = "{/color}")
    $ nvl_blue = Character(what_style="sub_blue", kind=nvl, 
        what_prefix="{color=#ADD8E6}", what_suffix = "{/color}",
        who_prefix="{color=#ADD8E6}", who_suffix = ":{/color}")

    $ style.create("sub_black", "default")
    $ style.sub_black.color = "#808080"
    $ char_black = Character(what_style="sub_black",
        what_prefix="{color=#808080}", what_suffix = "{/color}",
        who_prefix="{color=#808080}", who_suffix = "{/color}")
    $ nvl_black = Character(what_style="sub_black", kind=nvl, 
        what_prefix="{color=#808080}", what_suffix = "{/color}",
        who_prefix="{color=#808080}", who_suffix = ":{/color}")

    $ style.create("sub_null", "default")
    $ style.sub_null.color = "#000000"
    $ char_null = Character(what_style="sub_null",
        what_prefix="{color=#000000}", what_suffix = "{/color}",
        who_prefix="{color=#000000}", who_suffix = "{/color}")
    $ nvl_null = Character(what_style="sub_null", kind=nvl,
        what_prefix="{color=#000000}", what_suffix = "{/color}",
        who_prefix="{color=#000000}", who_suffix = ":{/color}")

    $ style.create("sub_orange", "default")
    $ style.sub_orange.color = "#F87431"
    $ char_orange = Character(what_style="sub_orange",
        what_prefix="{color=#F87431}", what_suffix = "{/color}",
        who_prefix="{color=#F87431}", who_suffix = "{/color}")
    $ nvl_orange = Character(what_style="sub_orange", kind=nvl,
        what_prefix="{color=#F87431}", what_suffix = "{/color}",
        who_prefix="{color=#F87431}", who_suffix = ":{/color}")

    $ style.create("sub_yellow", "default")
    $ style.sub_yellow.color = "#FFFF00"
    $ char_yellow = Character(what_style="sub_yellow",
        what_prefix="{color=#FFFF00}", what_suffix = "{/color}",
        who_prefix="{color=#FFFF00}", who_suffix = "{/color}")
    $ nvl_yellow = Character(what_style="sub_yellow", kind=nvl, 
        what_prefix="{color=#}", what_suffix = "{/color}",
        who_prefix="{color=#}", who_suffix = ":{/color}")

    $ style.create("sub_green", "default")
    $ style.sub_green.color = "#00FF00"
    $ char_green = Character(what_style="sub_green",
        what_prefix="{color=#00FF00}", what_suffix = "{/color}",
        who_prefix="{color=#00FF00}", who_suffix = "{/color}")
    $ nvl_green = Character(what_style="sub_green", kind=nvl, 
        what_prefix="{color=#00FF00}", what_suffix = "{/color}",
        who_prefix="{color=#00FF00}", who_suffix = ":{/color}")

    $ style.create("sub_white", "default")
    $ style.sub_white.color = "#FFFFFF"
    $ char_white = Character(what_style="sub_white",
        what_prefix="{color=#FFFFFF}", what_suffix = "{/color}",
        who_prefix="{color=#FFFFFF}", who_suffix = "{/color}")
    $ nvl_white = Character(what_style="sub_white", kind=nvl, 
        what_prefix="{color=#FFFFFF}", what_suffix = "{/color}",
        who_prefix="{color=#FFFFFF}", who_suffix = ":{/color}")

    $ style.create("sub_pink", "default")
    $ style.sub_pink.color = "#FAAFBE"
    $ char_pink = Character(what_style="sub_pink",
        what_prefix="{color=#FAAFBE}", what_suffix = "{/color}",
        who_prefix="{color=#FAAFBE}", who_suffix = "{/color}")
    $ nvl_pink = Character(what_style="sub_pink", kind=nvl, 
        what_prefix="{color=#FAAFBE}", what_suffix = "{/color}",
        who_prefix="{color=#FAAFBE}", who_suffix = ":{/color}")

    $ style.create("sub_purple", "default")
    $ style.sub_purple.color = "#6600CC"
    $ char_purple = Character(what_style="sub_purple", 
        what_prefix="{color=#6600CC}", what_suffix = "{/color}",
        who_prefix="{color=#6600CC}", who_suffix = "{/color}")
    $ nvl_purple = Character(what_style="sub_purple", kind=nvl, 
        what_prefix="{color=#6600CC}", what_suffix = "{/color}",
        who_prefix="{color=#6600CC}", who_suffix = ":{/color}")

    $ style.create("sub_forest", "default")
    $ style.sub_forest.color = "#00CC00"
    $ char_forest = Character(what_style="sub_forest",
        what_prefix="{color=#00CC00}", what_suffix = "{/color}",
        who_prefix="{color=#00CC00}", who_suffix = "{/color}")
    $ nvl_forest = Character(what_style="sub_forest", kind=nvl, 
        what_prefix="{color=#00CC00}", what_suffix = "{/color}",
        who_prefix="{color=#00CC00}", who_suffix = ":{/color}")   

    $ style.create("sub_tan", "default")
    $ style.sub_tan.color = "#FF9900"
    $ char_tan = Character(what_style="sub_tan",
        what_prefix="{color=#FF9900}", what_suffix = "{/color}",
        who_prefix="{color=#FF9900}", who_suffix = "{/color}")
    $ nvl_tan = Character(what_style="sub_tan", kind=nvl, 
        what_prefix="{color=#FF9900}", what_suffix = "{/color}",
        who_prefix="{color=#FF9900}", who_suffix = ":{/color}")   

    $ style.create("sub_red", "default")
    $ style.sub_red.color = "#FF0000"
    $ char_red = Character(what_style="sub_red",
        what_prefix="{color=#FF0000}", what_suffix = "{/color}",
        who_prefix="{color=#FF0000}", who_suffix = "{/color}")
    $ nvl_red = Character(what_style="sub_red", kind=nvl, 
        what_prefix="{color=#FF0000}", what_suffix = "{/color}",
        who_prefix="{color=#FF0000}", who_suffix = ":{/color}")

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
        
    if persistent.dev_commentary is None:
        persistent.dev_commentary = False

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
#These are our styles and whatnot
init -1:
    #$ renpy.watch("renpy.music.get_playing()", style = style.alertnow_text, xpos=0.0, xanchor='left', ypos=0.0, yanchor='bottom')
    $ renpy.watch("renpy.get_filename_line()", style = style.alertnow_text, xpos=1.0, xanchor='right', ypos=0.0, yanchor='top')
    if(config.developer):
        $ watch_header_rb = "In rollback: "
        $ renpy.watch("watch_header_rb + str(renpy.in_fixed_rollback())", style = style.alertnow_text, xpos=0.0, xanchor='left', ypos=0.76, yanchor='bottom')
        
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
    $ dev_screen = "None"
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
    
    define dev = Character('Developer', color="#FFFFFF", kind=char_white, show_two_window=True)
    $ scentered = Character(None, what_style="scentered_text", window_style="centered_window")
    $ narr = Character(None)
    $ nvldev = NVLCharacter('Developer', color="#FFFFFF", kind=nvl_white)
    $ nvln = NVLCharacter(None, kind=nvl)
    $ nvlcap = NVLCharacter(None, kind=nvl, ctc=anim.Blink("extra/arrow.png"))
    
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5
    style.quick_button.ypadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 17
    style.quick_button_text.idle_color = "#CC9900"
    style.quick_button_text.hover_color = "#CC0000"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#000000"
    
    # config.layers = [ 'premaster', 'master', 'postmaster', 'transient', 'screens', 'overlay' ]
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    config.windows_icon = "icon.png"
    config.window_icon = "icon.png"

    ## These values tell Ren'Py how to build a distribution.
    config.version = "v0.2.7_(1062)"
    config.log = config.gamedir + "/debuglog.txt"
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
    import renpy.store as store