init -1 python hide:
    from array import *

    layout.button_menu()

    # style.say_who_window.background = Frame("frame.png", 15, 15) #Background skin
    #style.say_who_window.xalign = 0.0
    #style.say_who_window.yalign = 1.0
    #style.say_who_window.xpos = 100 #For precise placement
    #style.say_who_window.ypos = 100 #For precise placement
    #style.say_who_window.left_padding = 15
    #style.say_who_window.top_padding = 15
    #style.say_who_window.right_padding = 15
    #style.say_who_window.bottom_padding = 15
    #style.say_who_window.xminimum = 150
    #style.say_who_window.yminimum = 15
    #style.say_who_window.xfill = False

    ## Please don't change this
    config.screen_width = 1200
    config.screen_height = 800

    #########################################
    #!URGENT : WE NEED OUR OWN THEME!#
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.
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

##############################################################################
# Say
# TODO: CLEANUP
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:
    tag say
    #show rpg stats code
    # automatically re-draw the GUI headers if necessary
    if(not in_debug):
        if(showMCStatus):#the normal stats
            $ show_combatant_stats(main_char, .02, .01)
        if(clock):#maybe we don't even need to check this variable...?
            $ Calendar()
            $ Clocks()
        if(ui_check):
            $ updateUI(intchange)
        if(walletshow):
            $ Wallet()
            
    ############################################
    # Defaults
    default side_image = None
    default two_window = False
    default doublespeak = False
    
    # Check for not doublespeak first
    if(not doublespeak):
        # Decide if we want to use the one-window or two-window varaint.
        if not two_window:
            # The one window variant.        
            window:
                id "window"
                has vbox:
                    style "say_vbox"
                if who:
                    text who id "who"
                text what id "what"
        else:
            # The two window variant.
            vbox:
                style "say_two_window_vbox"
                if who:            
                    window:
                        style "say_who_window"
                        text who:
                            id "who"
                window:
                    id "window"
                    has vbox:
                        style "say_vbox"
                    text what id "what"
        # If there's a side image, display it above the text.
        if side_image:
            add side_image
        else:
            add SideImage() xalign 0.0 yalign 1.0

    else:
        # Ignore SideImage
        if not two_window:
            # The one window variant.        
            window:
                xsize config.screen_width/2
                xalign 0.0
                id "window"
                has vbox:
                    style "say_vbox"
                if who:
                    text who.items()[0][0] id "who"
                text what[0] id "what" slow_cps True
            window:
                xsize config.screen_width/2
                xalign 1.0
                id "window"
                has vbox:
                    style "say_vbox"
                if who:
                    text who.items()[1][0] id "who"
                text what[1] id "what" slow_cps True
        else:
            # The two window variant.
            vbox:
                xsize config.screen_width/2
                style "say_two_window_vbox"
                if who:            
                    window:
                        style "say_who_window"
                        text who.items()[0][0]:
                            id "who"
                window:
                    id "window"
                    has vbox:
                        style "say_vbox"
                    text what[0] id "what" slow_cps True
            vbox:
                xsize config.screen_width/2
                xpos config.screen_width/2
                style "say_two_window_vbox"
                if who:            
                    window:
                        style "say_who_window"
                        text who.items()[1][0]:
                            id "who"
                window:
                    id "window"
                    has vbox:
                        style "say_vbox"
                    text what[1] id "what" slow_cps True
                    
    # Use the quick menu.
    use left_quick_menu
    use quick_menu
    if(battle_mode):
        $ renpy.block_rollback()



screen choice:
    $ in_menu = True
    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        vbox:
            style "menu"
            spacing 2
            for caption, action, chosen in items:
                if action:  
                    button:
                        action action
                        style "menu_choice_button"                        
                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"
    $ in_menu = False
        
init -2 python:
    config.narrator_menu = True
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu
        
##############################################################################
# Nvl
#
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl_hard:
    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"
screen nvl:
    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    use quick_menu
        
##############################################################################
# Main Menu 
#
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5
        xminimum 300
        has vbox

        textbutton _("Start Game") xminimum 300 action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Extras") action ShowMenu("more_menu")
        if(config.developer):
            textbutton "Run Newline Fixer" xminimum 300 action ui.callsinnewcontext("eol_change")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=True)
        textbutton "" action NullAction() style "empty_button"
        if config.developer:
            textbutton _("Persistent Reset") action ui.callsinnewcontext("destroy_persistent")
            textbutton "Seriously break things" action ui.callsinnewcontext("reset_button")
            textbutton "" action NullAction() style "empty_button"
        textbutton "Report a Bug" action Help("game/modules/report.html")
        textbutton "Check for Updates" action ui.callsinnewcontext("pre_update")
        textbutton "Dyslexic?" action ui.callsinnewcontext("dyslexic") text_style "dys_button_text"
        
screen more_menu:
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5
        xminimum 300
        has vbox
        
        textbutton _("Music Room") action (SetVariable('playing', name_playing()), ShowMenu("music_room", "nopredict"))
        textbutton "Gallery" xminimum 300 action ShowMenu("gallery")
        textbutton "" action NullAction() style "empty_button"
        textbutton "Glossary" action ShowMenu("glossary")
        textbutton _("Scene Replay") action ShowMenu("scene_replay")
        textbutton "Add-ons/Cheats" action ShowMenu("install_extras")
        #textbutton _("Credits") action ui.callsinnewcontext("credits")
        textbutton _("Return") action Return()


init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"
    


##############################################################################
# Navigation
#
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98
        
        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton "Glossary" action ShowMenu("glossary")
        if(persistent.debugmenu_installed):
            textbutton "Debug Menu" action ShowMenu("debug_menu")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    

##############################################################################
# Save, Load
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            
            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)
                    
            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5
                
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)
                    
                    # Format the description, and add it as text.
                    $ description = "% 2s. %s\n%s" % (
                        FileSlotName(i, columns * rows),
                        FileTime(i, empty=_("Empty Slot.")),
                        FileSaveName(i))

                    text (description) size 18

                    key "save_delete" action FileDelete(i)
                    
                    
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    


# Preferences
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") xminimum 300 action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")
           
            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton "Test":
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"
            frame:
                style_group "pref"
                has vbox

                label _("Voice Volume")
                bar value Preference("voice volume")

                if config.sample_voice:
                    textbutton "Test":
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"
            frame:
                style_group "pref"
                has vbox

                #label _("Change Rollback Mode")
                #if(not persistent.all_rollback):
                #    textbutton "Currently disabled\neverywhere" action ui.callsinnewcontext("rollback_mode")
                #elif(not persistent.choice_rollback):
                #    textbutton "Currently disabled\nat choices" action ui.callsinnewcontext("rollback_mode")
                #else:
                #    textbutton "Enabled\neverywhere" action ui.callsinnewcontext("rollback_mode")
                    
init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True
    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu

screen left_quick_menu:
    hbox:
        style_group "quick"
    
        xalign 0.0
        yalign 1.0
        textbutton _("Show Watches") action Function(show_watch)
        textbutton _("Hide Watches") action Function(unwatch, {"all":True})

screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 1.0
        yalign 1.0
        if(notin_other_stats):
            textbutton _("Stats") action ui.callsinnewcontext("other_stats")
        if(notin_other_stats and inventory_see):
            textbutton _("Items") action ui.callsinnewcontext("inventory_crap")
        if(has_phone):
            textbutton _("Phone") action ui.callsinnewcontext("inventory_crap")
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Save") action ShowMenu('save')
        #textbutton _("Skip") action Skip()
        #textbutton _("Auto") action Preference("auto-forward", "toggle")
        if(ingame == "Kazuki"):
            textbutton _("Memory") action ui.callsinnewcontext("audio_memory")
        if(not in_debug):
            textbutton _("Prefs") action ShowMenu('preferences')
            
screen updater:

    add "#000"

    frame:
        style_group ""

        xalign .5
        ypos 100
        xpadding 20
        ypadding 20

        xmaximum 400
        xfill True

        has vbox

        label _("Updater")

        null height 10

        if u.state == u.ERROR:
            text _("An error has occured:")
        elif u.state == u.CHECKING:
            text _("Checking for updates.")
        elif u.state == u.UPDATE_NOT_AVAILABLE:
            text _("This program is up to date.")
        elif u.state == u.UPDATE_AVAILABLE:
            text _("[u.version] is available.\nYou have: [build.directory_name]. Do you want to update?")
        elif u.state == u.PREPARING:
            text _("Preparing to download the updates.")
        elif u.state == u.DOWNLOADING:
            text _("Downloading the updates.")
        elif u.state == u.UNPACKING:
            text _("Unpacking the updates.")
        elif u.state == u.FINISHING:
            text _("Finishing up.")
        elif u.state == u.DONE:
            text _("The updates have been installed. The program will restart.")
        elif u.state == u.DONE_NO_RESTART:
            text _("The updates have been installed.")
        elif u.state == u.CANCELLED:
            text _("The updates were cancelled.")

        if u.message is not None:
            null height 10
            text "[u.message!q]"

        if u.progress is not None:
            null height 10
            bar value u.progress range 1.0 style "_bar"

        if u.can_proceed or u.can_cancel:
            null height 10

        if u.can_proceed:
            textbutton _("Proceed") action u.proceed xfill True

        if u.can_cancel:
            textbutton _("Cancel") action u.cancel xfill True