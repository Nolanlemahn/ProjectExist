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
        if(in_game):
            textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        if(in_game):
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
