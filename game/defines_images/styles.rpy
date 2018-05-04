# start styles: Theme
init -1 python hide:
    from array import *

    layout.button_menu()
    # style.say_who_window.background = Frame("frame.png", 15, 15) #Background skin

    #########################################
    #!URGENT : WE NEED OUR OWN THEME!#
    theme.threeD(
        # Color scheme: Colorblind
                                    
        ## The color of an idle widget face.
        widget = "#898989",

        ## The color of a focused widget face.
        widget_hover = "#464646",

        ## The color of the text in a widget.
        widget_text = "#CCCCCC",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#F2F2F2",

        ## The color of a disabled widget face. 
        disabled = "#898989",

        ## The color of disabled widget text.
        disabled_text = "#666666",

        ## The color of informational labels.
        label = "#c2c2c2",

        ## The color of a frame containing widgets.
        frame = "#252525",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "drops/menu.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#393939",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )

    style.window.background = Frame("menus/FoxDialogueBox.png", 25, 25)
    style.frame.background = Frame("menus/FoxFrameBox.png", 25, 25)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is
    ## drawn.

    # style.window.left_padding = 6
    # style.window.right_padding = 6
    # style.window.top_padding = 6
    # style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins
    ## and padding.

    # style.window.yminimum = 250

    style.default.font = checkDefaultFont()
    style.default.size = checkDefaultSize()

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = True
    config.has_autosave = False
    style.empty_button = Style(style.button_text)
    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    # config.main_menu_music = "main_menu_theme.ogg"

    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = dissolve

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolve

    ## Used between screens of the game menu.
    config.intra_transition = dissolve

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = dissolve

    ## Used when returning to the main menu from the game.
    config.game_main_transition = dissolve

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = dissolve

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = dissolve

    ## Used when a game is loaded.
    config.after_load_transition = dissolve

    ## Used when the window is shown.
    config.window_show_transition = dissolve

    ## Used when the window is hidden.
    config.window_hide_transition = dissolve
init -1 python:
    style.clipFrame = Style(style.frame)
    style.clipFrame.background = Frame("menus/FoxFrameClip.png", 25, 25)
    
    style.nvl_menu_choice.idle_color = "#ffffffff"
    style.nvl_menu_choice.hover_color = "#ccccccff"
    style.nvl_menu_choice_button.hover_background = "#00000000"
    style.nvl_menu_choice_button.left_margin = 0
    
    style.mm_button.background = Frame("menus/FoxButtonBox.png", 25, 25)
    style.mm_button.hover_background = Frame("menus/FoxButtonHover.png", 25, 25)

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
init -1:
    $ style.create("game_box", "frame")
    $ style.game_box.background = Frame("menus/FoxGameBox.png", 25, 25)
# end styles: UI

# start styles: Characters
    style scentered_text:
        textalign 0.5
        xalign 0.5
        yalign 0.5
        layout "subtitle"
        font "fonts/Respective_Slanted.ttf"
        size 64
    
    
    $ style.alert_text.color = "#FF0000"
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

    $ style.create("sub_teal", "default")
    $ style.sub_teal.color = "#46C6C6"
    $ char_teal = Character(what_style="sub_teal",
        what_prefix="{color=#46C6C6}", what_suffix = "{/color}",
        who_prefix="{color=#46C6C6}", who_suffix = "{/color}")
    $ nvl_teal = Character(what_style="sub_teal", kind=nvl, 
        what_prefix="{color=#46C6C6}", what_suffix = "{/color}",
        who_prefix="{color=#46C6C6}", who_suffix = ":{/color}")

    $ style.create("sub_bubgum", "default")
    $ style.sub_bubgum.color = "#CC6699"
    $ char_bubgum = Character(what_style="sub_bubgum",
        what_prefix="{color=#CC6699}", what_suffix = "{/color}",
        who_prefix="{color=#CC6699}", who_suffix = "{/color}")
    $ nvl_bubgum = Character(what_style="sub_bubgum", kind=nvl, 
        what_prefix="{color=#CC6699}", what_suffix = "{/color}",
        who_prefix="{color=#CC6699}", who_suffix = ":{/color}")

init -1:
    define dev = Character('Developer', color="#FFFFFF", kind=char_white)
    $ scentered = Character(None, what_style="scentered_text", window_style="centered_window")
    $ narr = Character(None)
    $ nvldev = NVLCharacter('Developer', color="#FFFFFF", kind=nvl_white)
    $ nvln = NVLCharacter(None, kind=nvl)
    $ nvlcap = NVLCharacter(None, kind=nvl, ctc=anim.Blink("extra/arrow.png"))
#end styles: Characters
    
