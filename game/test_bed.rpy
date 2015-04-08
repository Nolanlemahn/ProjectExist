label blog_post:
    nvln "[[Side note: new build tomorrow fixing a few typos in the glossary and a few other places.]\n\nIf you were to ask me, one of the most
           annoying things about... life in general really... would be realizing two specific problems at the exact same moment.\n\n
          The first would be that of \"not knowing\" something. Which shouldn't be so bad on its own, since it's basically impossible to
          know everything about everything (if that makes any sense). It might grind your gears that you don't have the information, but
           hopefully you could get it at some point."

label backup:
    $ m1status = "stunned"
    $ m1mess2 = check_status("m1")
    $ m1mess2 = m1mess2[1]
    "[m1mess2]"
    
label requested_start_cb:
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
    $ main_known_moves = [1,2,3,0,0,0,0,0]
    $ answers = []
    $ answer_add("self_40")
    $ flags = []
    $ points = init_points()
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
    
    #show screen fake_say
    #[scene1
    $ clock = False
    $ walletshow = False
    $ main_char_show_rpg = True
    $ main_name = "Kazuki"
    $ clock = True
    $ walletshow = True
    $ minutes = 1
    $ jumping_in = True
    jump cb_test
    
label cb_test:
    $ enemy_name = "???"
    $ enemy_level = 4
    $ enemy_maxHP = 60
    $ enemy_currentHP = 60
    $ enemy_maxBelly = 100
    $ enemy_currentBelly = 100
    $ enemy_maxSleep = 100
    $ enemy_currentSleep = 100
    $ enemy_maxXP = 35
    $ enemy_currentXP = 0
    $ enemy_STR = 24
    $ enemy_DEX = 7
    $ enemy_RES = 6
    $ enemy_SPD = 2
    $ enemy_INT = 9
    $ enemy_SPI = 24
    $ enemy_ABI_SLO1 = "No ability"
    $ enemy_ABI_SLOL1 = 0
    $ enemy_ABI_SLO2 = "No ability"
    $ enemy_ABI_SLOL2 = 0
    $ enemy_RS_SLO1 = "No symbol"
    $ enemy_RS_SLOL1 = 0
    $ enemy_RS_SLO2 = "No symbol"
    $ enemy_RS_SLOL2 = 0
    $ enemy_weapon = "Fists"
    $ enemy_armor = "Nothing"
    $ enemy_known_moves = [1,0,0,0]
    $ enemy_ai_type = "firstfoe"
    $ precursor = "none"
    $ progress = "001"
    call a1v1fight(main_known_moves, main_name, main_char_level, main_char_currentHP, main_char_maxHP, main_char_currentBelly, main_char_maxBelly, main_char_currentSleep, main_char_maxSleep, main_char_stats, main_char_ABI_SLO1, main_char_ABI_SLOL1, main_char_ABI_SLO2, main_char_ABI_SLOL2, main_char_RS_SLO1, main_char_RS_SLOL1, main_char_RS_SLO2, main_char_RS_SLOL2, main_char_currentXP, main_char_maxXP, enemy_known_moves, enemy_name, enemy_level, enemy_currentHP, enemy_maxHP,
        enemy_currentBelly, enemy_maxBelly, enemy_currentSleep, enemy_maxSleep, enemy_STR, enemy_DEX, enemy_RES, enemy_SPD, enemy_INT, enemy_SPI, enemy_currentXP, enemy_maxXP, enemy_ai_type, precursor)
    "Good fight?"
    return