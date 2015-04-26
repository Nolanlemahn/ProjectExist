﻿init python:
    scopes = {}
    special_cases = ["combat_test"]
    base_scope={'ingame':"Kazuki",
        'main_name':"?",
        'main_type':"kk",
        'main_char_level':5,
        'main_char_maxHP':100,
        'main_char_currentHP':100,
        'main_char_maxBelly':100,
        'main_char_currentBelly':65,
        'main_char_maxSleep':100,
        'main_char_currentSleep':75,
        'main_char_maxXP':50,
        'main_char_currentXP':0,
        'main_char_stats':[11,11,20,14,14,20],
        'main_char_ABI_SLO1':"No ability",
        'main_char_ABI_SLOL1':0,
        'main_char_ABI_SLO2':"No ability",
        'main_char_ABI_SLOL2':0,
        'main_char_RS_SLO1':"No symbol",
        'main_char_RS_SLOL1':0,
        'main_char_RS_SLO2':"No symbol",
        'main_char_RS_SLOL2':0,
        'main_char_weapon':"Fists",
        'main_char_armor':"Nothing",
        'main_known_moves':[1,2,0,0,0,0,0,0],
        'answers':[],
        'flags':[],
        'points':init_points(),
        'reminders':[],
        'j_name':"Jonathan",
        'theweekday':3,
        'themonth':9,
        'theday':21,
        'theyear':2010,
        'dayofyear':264,
        'yearlim':365,
        'daylim':30,
        'stringweekday':"Tuesday",
        'stringmonth':"September",
        'main_char_cash':200.00,
        'has_phone':False,
        'corruption':0,
        'walletshow':True,
        'main_char_show_rpg':True,
        'ui_check':False,
        'strchange':"",
        'progress':"000",
        'shadow_name':"Shadow",
        's':DynamicCharacter("shadow_name", color="#808080", kind=char_black, show_two_window=True),
        'nvls':DynamicCharacter("shadow_name", color="#808080", kind=nvl_black),
        'mtname':"Math Teacher",
        'mt':DynamicCharacter("mtname", show_two_window=True),
        'dname':"\"Father\"",
        'd':DynamicCharacter("dname", show_two_window=True),
        'r':Character('Rin', color="#000000", kind=char_null, show_two_window=True),
        'nvlr':Character('Rin', color="#000000", kind=nvl_null),
        'l':Character('Lawrence', color='#F87431', kind=char_orange, show_two_window=True),
        'nvll':Character('Lawrence', color='#F87431', kind=nvl_orange),
        'j':DynamicCharacter("j_name", color="#ADD8E6", kind=char_blue, show_two_window=True),
        'nvlj':DynamicCharacter("j_name", color="#ADD8E6", kind=nvl_blue),
        'n':Character('Natalie', color='#FAAFBE', kind=char_pink, show_two_window=True),
        'nvlnb':Character('Natalie', color='#FAAFBE', kind=nvl_pink),
        't':Character('Tammy', color='#00FF00', kind=char_green, show_two_window=True),
        'nvlt':Character("Tammy", color='#00FF00', kind=nvl_green),
        'w':Character('Wil', color="#FFFF00", kind=char_yellow, show_two_window=True),
        'nvlt':Character('Wil', color="#FFFF00", kind=nvl_yellow),
        'b':Character('Ben', color="#6600CC", kind=char_purple, show_two_window=True),
        'nvlb':Character('Ben', color="#6600CC", kind=nvl_purple),
        'li':Character('Lilian', color="#00CC00", kind=char_forest, show_two_window=True),
        'nvlli':Character('Lilian', color="#00CC00", kind=nvl_forest),
        'ro':Character('Robert', color="#FF9900", kind=char_tan, show_two_window=True),
        'nvlro':Character('Robert', color="#FF9900", kind=nvl_tan),
        'a':Character('Athena', color="#FF0000", kind=char_red, show_two_window=True),
        'nvla':Character('Athena', color="#FF0000", kind=nvl_red),
        'mc':DynamicCharacter("main_name", color="#C0C0C0", kind=char_gray, show_two_window=True),
        'nvlmc':DynamicCharacter("main_name", color="#C0C0C0", kind=nvl_gray),
        'nmc':Character(None, what_style="main_gray"),
        'nnvlmc':Character(None, color="#C0C0C0", kind=nvl_gray_narr),
        'minutes':460,
        'clock':True,
        'in_side_note':False}
    #==============
    scopes["Kazuki_1b"]={'main_name':"Kazuki"}
    scopes["Kazuki_1c"]={'main_name':"Kazuki",
        'main_char_currentBelly':70,
        'answers':["law_hesitation", "nat_will_try"],
        'minutes':596,
        'points':[-2, 0, 0, 0, 0, 0, 0, 0]}
        