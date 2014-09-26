#support
init python:
    def mlib(selection):
        #bgm
        if(selection == "room3"):
            renpy.music.play("bgm/room3.mp3", loop=True, fadein=1.0)
        if(selection == "round"):
            renpy.music.play("bgm/the_round.mp3", loop=True, fadein=1.0)
            
        #these sfxs act as bgm, but do not constitute "music" in their own rights
        #as such, we will not mark them as unlocked
        if(selection == "march"):
            renpy.music.play("bgm/march_lit.wav", loop=True)
        if(selection == "calarm"):
            renpy.music.play("sfx/clock_alarm.wav", loop=True)
        if(selection == "falarm"):
            renpy.music.play("sfx/domestic_falarm.mp3", loop=True)
            
        #sfxs
        if(selection == "cskid"):
            renpy.sound.play("sfx/car_skid.mp3")
            renpy.pause(2.0)
        return
        
image empty = "drops/empty.png"

#countdowns
image countdown 1 = DynamicDisplayable(countdown, length=1.0)
image countdown 4 = DynamicDisplayable(countdown, length=4.0)
image countdown 5 = DynamicDisplayable(countdown, length=5.0)
image countdown 7 = DynamicDisplayable(countdown, length=7.0)
image countdown 10 = DynamicDisplayable(countdown, length=10.0)
image countdown 15 = DynamicDisplayable(countdown, length=15.0)
image countdown 20 = DynamicDisplayable(countdown, length=20.0)
image countdown 30 = DynamicDisplayable(countdown, length=30.0)

#bg - support
image bg blackdrop = "#000000"
image bg graydrop = "drops/graydrop.png"
image bg mainmenu = "drops/menu.png"

#characters

#bg generic
image bg fog = "drops/fog.png"
image bg fakefog = "drops/sneakfog.png"
image bg city1 = "drops/city1.png" #a generic picture of the outside of sacramento
image bg city1 blur = "drops/city1blur.png" #a generic picture of the outside of sacramento, but blurry (Kazuki is running)
image bg classroom1 = "drops/classroom1.png" #lawrence's classroom
image bg classroom2 = "drops/classroom2.png" #tamara's classroom
image bg classroom3 = "drops/classroom3.png" #math classroom
image bg hallway1 = "drops/hallway1.png" #some hallway in the college
image bg window1 = "drops/window1.png" #outside tamara's window
image bg stairwell1 = "drops/stairwell1.png" #stairs of the school
image bg parkinglot1 = "drops/parkinglot1.png" #parkinglot of the school
image bg bus1 = "drops/bus1.png" #public bus
image bg bus2 = "drops/bus2.png" #public bus
image bg library1 = "drops/library1.png"
image bg workshop = "drops/workshop.png"

#kazuki
image bg kazuki bed = "drops/kazuki/bed.png"
image bg kazuki bathroom = "drops/kazuki/bathroom.png"
image bg kazuki journal = "drops/kazuki/journal.png"
image bg kazuki bedroom = "drops/kazuki/bedroom.png"
image bg kazuki kitchen = "drops/kazuki/kitchen.png"
image asset flier last = "extra/flier_last.png"


#sidenotes
image sn demo = DynamicDisplayable(show_sn, tt=
    "This is a demo side note. You may click to dismiss, or you may progress to the next dialogue screen. It will dismiss itself after three "+
    "interactions.")
image sn gre = DynamicDisplayable(show_sn, tt=
    "GRE is short for Graduate Record Examination, a standardized test developed by " + 
    "the Educational Testing Service (ETS) in the United States in order to measure and compare graduate school candidates.")
image sn siebener = DynamicDisplayable(show_sn, tt=
    "A Siebener refers to a 7 series BMW, just as a bimmer refers to any BMW car. A beemer actually refers to a motorcycle made by BMW.")
image sn frank = DynamicDisplayable(show_sn, tt=
    "Frank Anthoni Bruni was the chief restaurant critic of the New York Times from 2004 to 2009.")

init -1:
    #styles - ui
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
    if persistent.useDyslexic is None:
        persistent.useDyslexic = False
    if persistent.amDev is None:
        persistent.amDev = False
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

#These are our styles and whatnot
init -1:
    $ playing = "nothing"
    $ renpy.watch("renpy.music.get_playing()", style = style.alertnow_text, xpos=0.0, xanchor='left', ypos=0.0, yanchor='bottom')
    $ renpy.watch("renpy.get_filename_line()", style = style.alertnow_text, xpos=1.0, xanchor='right', ypos=0.0, yanchor='top')
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
    
    style scentered_text:
        textalign 0.5
        xalign 0.5
        yalign 0.5
        layout "subtitle"
        font "Respective_Slanted.ttf"
        size 64
    
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
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    config.version = "v0.2.5_(1031)"
    build.directory_name = "ProjEx_" + config.version
    build.executable_name = "Project Exist"
    build.include_update = True
    build.classify('**samples**', None)#!!
    build.classify('***/Project_Exist*.zip', None)
    build.classify('files/**', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("**.rpy", None)
    ## To archive files, classify them as 'archive'.
    
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    build.documentation('*.html')
    build.documentation('*.txt')
    #build.documentation('*.pdf')
    
#Implemented wtf_iorpy_magic.
#Worked around an NVL crash in the Glossary.
#Removed some broken menus.

init python:
    adj=user_adjustment
    import renpy.store as store