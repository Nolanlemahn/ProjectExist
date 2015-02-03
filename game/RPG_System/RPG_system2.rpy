label a1v1fight(m1_known_moves, m1name, m1level, m1hp, m1maxhp, m1fp, m1maxfp, m1sp, m1maxsp, m1stats, m1_ABI_SLO1, m1_ABI_SLOL1, m1_ABI_SLO2, m1_ABI_SLOL2, m1_RS_SLO1, m1_RS_SLOL1, m1_RS_SLO2, m1_RS_SLOL2, m1XP, m1maxXP, e1_known_moves, e1name, e1level, e1hp, e1maxhp, e1fp, e1maxfp, e1sp, e1maxsp, e1STR, e1DEX, e1RES, e1SPD, e1INT, e1SPI, e1XP, e1maxXP, eAIT, precursor):
    window show#chances are high that we forgot to do this
    $ fight_is_1v1 = True
    $ firstturn = True
    $ batcheckpoint = 0
    $ curr_eval = "m1"
    $ battle_current = True
    call load_moves_part1(m1_known_moves)
    return

label m1_1v1_turnb:
    "What will [m1name] do?{fast}{nw}"
    menu:
        extend "{fast}"
        "Fight":
            jump m1_1v1_turnc
        "Bag":
            jump battle_inventory
        "Switch":
            "There's no one to switch with...{fast}"
            jump m1_1v1_turnb
        "Run":
            "[m1name] is not a coward and refuses to run!{fast}"
            jump m1_1v1_turnb
    
label m1_1v1_turnc:
    menu:
        extend "{fast}"
        "%(movename1)s" if (moveexists > 0):
            $ chosenmove = movename1
            pass
        "%(movename2)s" if (moveexists > 1):
            $ chosenmove = movename2
            pass
        "%(movename3)s" if (moveexists > 2):
            $ chosenmove = movename3
            pass
        "%(movename4)s" if (moveexists > 3):
            $ chosenmove = movename4
            pass
        "%(movename5)s" if (moveexists > 4):
            $ chosenmove = movename5
            pass
        "%(movename6)s" if (moveexists > 5):
            $ chosenmove = movename6
            pass
        "(Get move information on known moves)":
            jump get_move_info
        "(Do something else)":
            jump m1_1v1_turnb
    if(battle_current):
        call load_moves_part3(chosenmove)
    return
    #...

label get_move_info:
    #tempa-broken
    "Which move would you like more information on?{fast}{nw}"
    menu:
        extend "{fast}"
        "%(movename1)s" if (moveexists > 0):
            $ chosenmove = movename1
            pass
        "%(movename2)s" if (moveexists > 1):
            $ chosenmove = movename2
            pass
        "%(movename3)s" if (moveexists > 2):
            $ chosenmove = movename3
            pass
        "%(movename4)s" if (moveexists > 3):
            $ chosenmove = movename4
            pass
        "%(movename5)s" if (moveexists > 4):
            $ chosenmove = movename5
            pass
        "%(movename6)s" if (moveexists > 5):
            $ chosenmove = movename6
            pass
        "%(movename7)s" if (moveexists > 6):
            $ chosenmove = movename6
            pass
        "%(movename8)s" if (moveexists > 7):
            $ chosenmove = movename6
            pass
        "(Do something else)":
            jump m1_1v1_turnb
    call about_move(chosenmove)

label inventory_crap:
    $ inventory_see = False
    $ notin_other_stats = False
    window show
    with dissolve
    nvln "Not working atm."
    window hide
    with dissolve
    nvl clear
    $ inventory_see = True
    $ notin_other_stats = True
    return
    
label battle_inventory:
    window show
    with dissolve
    nvln "Not working atm."
    window hide
    with dissolve
    nvl clear
    jump m1_1v1_turnb
    
label other_stats:#show combat stats
    $ notin_other_stats = False
    window show
    with dissolve
    if(not ingame):
        nvln "Progress farther in the game to use this screen."
    else:
        nvln "(Expect this screen to be unavailable in non-dev/debug mode in the final release.)\nStrength: [main_char_stats[0]]\nDexterity: [main_char_stats[1]]\nSpeed: [main_char_stats[2]]\nResilience: [main_char_stats[3]]\nIntelligence: [main_char_stats[4]]\nSpirit: [main_char_stats[5]]\nAbility 1: [main_char_ABI_SLO1] || Level [main_char_ABI_SLOL1]\nAbility 2: [main_char_ABI_SLO2] || Level [main_char_ABI_SLOL2]"
    window hide
    with dissolve
    nvl clear
    $ notin_other_stats = True
    return

init python:
    def domchange(passedvar, passedvalue, bool_loud):
        renpy.call("domchange", passedvar, passedvalue, bool_loud)
        return
   
label domchange(passedvar, passedvalue, bool_loud):
    if passedvalue > 0:
        $ strchange = "+" + str(passedvalue) + " " +  passedvar
    else:
        $ strchange = str(passedvalue) + " " +  passedvar
    if(passedvar == "HP"):
        if(not fight_is_1v1):
            $ main_char_currentHP = main_char_currentHP + passedvalue
    elif(passedvar == "FP"):
        if(not fight_is_1v1):
            $ main_char_currentBelly = main_char_currentBelly + passedvalue
    elif(passedvar == "SP"):
        if(not fight_is_1v1):
            $ main_char_currentSleep = main_char_currentSleep + passedvalue
    if(bool_loud == 1):
        $ updateUIroutine = 2
    return