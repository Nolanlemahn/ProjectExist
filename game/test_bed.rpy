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
    
label test:
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
    return