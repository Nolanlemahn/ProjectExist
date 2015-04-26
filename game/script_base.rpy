init -1:
    $ answers = []

label start:#this_label_done
    $ answers = []
    $ showMCStatus = False
    $ in_side_note = False
    show screen mlib_listener
    scene bg blackdrop
    with dissolve
    #jump test_iorpy_magic
    $ snroutine = -1
    $ selected_note = ""
    #$ renpy.say(None, os.path.abspath(config.savedir))
    #$ save_name = begin_game()
    #$ renpy.block_rollback()
    #narr "This is a friendly reminder to go to the Options menu, and choose whether or not you would like Rollback to be enabled, and whether or not you want Developer/Writer commentary. By default, Rollback is disabled, and commentary is disabled."
    if (persistent.standalone_dlc_avail):
        "There is standalone DLC installed and unlocked. Would you like to launch one of those instead of the main game?"
        menu:
            extend ""
            "Yes":
                jump standalone_dlc_menu
            "No":
                $ python_pass()
    narr "Which character would you like to play as? Each character has a different story and different available sub-routes, but the game universe does not change."
    menu:
        extend ""
        "Kazuki (Main male character)":
            call rollfind
            jump Kazuki_1a
        "Katherine (Main female character)":
            call rollfind
            jump Rin_1a
    #end_of_label

label after_load:
    return

label standalone_dlc_menu:
    "Which DLC would you like to launch?"
    menu:
        extend ""
        "DLC#1: Prologue" if (persistent.dlc1_installed and renpy.has_label('dlc1_1a')):
            jump dlc1_1a
        "Cancel (Main game)":
            jump alternative_start
            
label alternative_start:#this_label_done
    "Which character would you like to play as? Each character has a different story and different available partners, but the game universe does not change."
    menu:
        extend ""
        "Kazuki (Main male character)":
            call rollfind
            jump Kazuki_1a
        "Katherine (Main female character)":
            call rollfind
            jump Rin_1a
            
label dead_end: #
    $ battle1_mode = False
    $ battle_mode = False
    call rollfind
    "The game has ended for an unknown reason. The most likely reason is an attempt to access a currently unimplemented path, or you have completed as much of a path as is available."
    return

label text_died_of_hunger:
    call rollfind
    $ single_death_check = True
    "You have died of hunger!"
    return

label text_died_of_sleep:
    call rollfind
    $ single_death_check = True
    "You have died of sleep deprivation!"
    return
    
label end_of_day:
    call rollfind
    jump dead_end #-TEMP-

label credits:
    scene bg blackdrop
    nvln "PyTom: Lots of help with callbacks, arrays, and Character() nonsense."
    nvln "http://www.freesfx.co.uk: {a=http://www.freesfx.co.uk/soundeffects/sirens/}Fire alarm sound{/a}."
    nvln "http://wallpaper-million.com: {a=http://wallpaper-million.com/download/Motion-blur-night-panorama-wallpaper_3446.html}Blurred?{/a}."
    nvln "quicktime115: A very special proofreader."
    nvln "Domo: One of the evil users. <3"
    nvln "delta: readback.rpy"
    nvln "Måns Grebäck: Respective font."
    nvln "Soundbible.com: {a=http://soundbible.com/61-City-Car-Horn.html}car horn sound{/a}."
    nvln "UncleKornicob: {a=http://soundbible.com/1787-Annoying-Alarm-Clock.html}alarm clock sound{/a}."
    nvln "The DavisWiki: {a=http://daviswiki.org/Memorial_Union}A single picture{/a}."
    nvl clear