label requested_start_k:
    $ in_side_note = False
    scene bg blackdrop
    with dissolve
    #jump test_iorpy_magic
    $ snroutine = -1
    $ selected_note = ""
    #$ renpy.say(None, os.path.abspath(config.savedir))
    #$ save_name = begin_game()
    $ renpy.block_rollback()
    $ ingame = "Kazuki"
    $ main_name = "?"
    $ main_type = "kk"
    $ main_char_level = 5
    # start implementing the table of stats
    $ main_char_maxHP = 100
    $ main_char_currentHP = 100
    $ main_char_maxBelly = 100
    $ main_char_currentBelly = 65
    $ main_char_maxSleep = 100
    $ main_char_currentSleep = 75
    $ main_char_maxXP = 50
    $ main_char_currentXP = 0
    $ main_char_stats = [11,11,20,14,14,20]
    # STR, DEX, RES, SPD, INT, SPI
    $ main_char_ABI_SLO1 = "No ability"
    $ main_char_ABI_SLOL1 = 0
    $ main_char_ABI_SLO2 = "No ability"
    $ main_char_ABI_SLOL2 = 0
    $ main_char_RS_SLO1 = "No symbol"
    $ main_char_RS_SLOL1 = 0
    $ main_char_RS_SLO2 = "No symbol"
    $ main_char_RS_SLOL2 = 0
    $ main_char_weapon = "Fists"
    $ main_char_armor = "Nothing"
    $ main_known_moves = [1,2,0,0,0,0,0,0]
    $ answers = []
    $ flags = []
    $ points = []
    $ init_points()
    $ reminders = []
    $ j_name = "Jonathan"
    #[needed for clocks + alert
    $ theweekday = 3#tuesday
    $ themonth = 9
    $ theday = 21
    $ theyear = 2010
    $ dayofyear = 264
    $ yearlim = 365
    $ daylim = 30
    $ stringweekday = "Tuesday"
    $ stringmonth = "September"    
    $ main_char_cash = 200.00
    $ has_phone = False
    
    #]
    $ walletshow = True
    $ main_char_show_rpg = True
    $ ui_check = False
    $ strchange = ""
    $ progress = "000"
    
    ###########
    
    $ shadow_name = "Shadow"
    $ s = DynamicCharacter("shadow_name", color="#808080", kind=char_black, show_two_window=True)
    $ nvls = DynamicCharacter("shadow_name", color="#808080", kind=nvl_black)
    ###########
    
    $ mtname = "Math Teacher"
    $ mt = DynamicCharacter("mtname", show_two_window=True)
    
    $ dname = "\"Father\""
    $ d = DynamicCharacter("dname", show_two_window=True)

    #Rin
    $ r = Character('Rin', color="#000000", kind=char_null, show_two_window=True)
    $ nvlr = Character('Rin', color="#000000", kind=nvl_null)
    
    #Lawrence
    $ l = Character('Lawrence', color='#F87431', kind=char_orange, show_two_window=True)
    $ nvll = Character('Lawrence', color='#F87431', kind=nvl_orange)
    
    #Jonathan
    $ j = DynamicCharacter("j_name", color="#ADD8E6", kind=char_blue, show_two_window=True)
    $ nvlj = DynamicCharacter("j_name", color="#ADD8E6", kind=nvl_blue)
    
    #Natalie
    $ n = Character('Natalie', color='#FAAFBE', kind=char_pink, show_two_window=True)
    $ nvlnb = Character('Natalie', color='#FAAFBE', kind=nvl_pink)
    
    #Tamara
    $ t = Character('Tammy', color='#00FF00', kind=char_green, show_two_window = True)
    $ nvlt = Character("Tammy", color='#00FF00', kind=nvl_green)
    
    #Wil
    $ w = Character('Wil', color="#FFFF00", kind=char_yellow, show_two_window = True)
    $ nvlt = Character('Wil', color="#FFFF00", kind=nvl_yellow)
    
    #Ben
    $ b = Character('Ben', color="#6600CC", kind=char_purple, show_two_window = True)
    $ nvlb = Character('Ben', color="#6600CC", kind=nvl_purple)

    #Lilian
    $ li = Character('Lilian', color="#00CC00", kind=char_forest, show_two_window = True)
    $ nvlli = Character('Lilian', color="#00CC00", kind=nvl_forest)
    
    #Robert
    $ ro = Character('Robert', color="#FF9900", kind=char_tan, show_two_window = True)
    $ nvlro = Character('Robert', color="#FF9900", kind=nvl_tan)
    
    #Athena
    $ a = Character('Athena', color="#FF0000", kind=char_red, show_two_window = True)
    $ nvla = Character('Athena', color="#FF0000", kind=nvl_red)
    
    ###########
    
    #Kazuki
    $ mc = DynamicCharacter("main_name", color="#C0C0C0", kind=char_gray, show_two_window=True)#standardmain
    $ nvlmc = DynamicCharacter("main_name", color="#C0C0C0", kind=nvl_gray)#nvlmain
    
    #Internal Kazuki
    $ nmc = Character(None, what_style="main_gray")#thinkmain
    $ nnvlmc = Character(None, color="#C0C0C0", kind=nvl_gray_narr)#nvl-thinkmain
    
    $ dev_screen = "pass"
    #show screen fake_say
    #[scene1
    $ clock = False
    $ walletshow = False
    $ main_char_show_rpg = True
    $ main_name = "Kazuki"
    $ clock = True
    $ walletshow = True
    jump Kazuki_1j_lunch

label start:#this_label_done
    $ in_side_note = False
    scene bg blackdrop
    with dissolve
    #jump test_iorpy_magic
    $ snroutine = -1
    $ selected_note = ""
    #$ renpy.say(None, os.path.abspath(config.savedir))
    #$ save_name = begin_game()
    $ renpy.block_rollback()
    #narr "This is a friendly reminder to go to the Options menu, and choose whether or not you would like Rollback to be enabled, and whether or not you want Developer/Writer commentary. By default, Rollback is disabled, and commentary is disabled."
    call dev_com(1)
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