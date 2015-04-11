label m1_1v1_turna:
    "What will [m1name] do?{fast}{nw}"
    menu:
        extend "{fast}"
        "Fight":
            jump m1_1v1_turnb
        "Bag":
            jump battle_inventory
        "Switch":
            "There's no one to switch with...{fast}"
            jump m1_1v1_turna
        "Run":
            "[m1name] is not a coward and refuses to run!{fast}"
            jump m1_1v1_turna
    return

label m1_1v1_turnb:
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
            jump m1_1v1_turna
    if(battle_current):
        $ cbm[chosenmove].assign("m1", chosenmove)
        call load_moves_part3(chosenmove)
    return

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
            jump m1_1v1_turna
    call about_move(chosenmove)
    return

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
    jump m1_1v1_turna
    
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
    