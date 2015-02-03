label battle_end:
    $ single_combat_check = True
    "It's over..."
    $ fight_is_1v1 = False
    $ battle_current = False
    #if (progress == "001")
    return#TODO implement jumping back

label battle_death:
    $ single_combat_check = True
    "It's over..."
    $ battle_current = False
    return

label load_moves_part1(moveset):#player1
    $ movecount = 0
    $ moveexists = 0
    while (movecount < 8):
        if (moveset[movecount] == 0):
            $ movenames[movecount] = "DNE"
        if (moveset[movecount] >= 1):
            $ moveexists = moveexists + 1
            $ movenames[movecount] = cbm.keys()[movecount + 1]
            $ movecosts[2 * movecount] = cbm[cbm.keys()[movecount + 1]].cost[0]
            $ movecosts[2 * movecount + 1] = cbm[cbm.keys()[movecount + 1]].cost[1]
        
        # ADDMOREMOVES
        $ movecount = movecount + 1
    ##begin checking symbols and innate abilities
    #write this code later it's not needed yet
    if (moveexists == 0):
        $ moveexists = 1
        $ movenames[0] = "Struggle"
    $ movecount = 0
    $ movename1 = movenames[0]
    $ movename2 = movenames[1]
    $ movename3 = movenames[2]
    $ movename4 = movenames[3]
    $ movename5 = movenames[4]
    $ movename6 = movenames[5]
    $ movename7 = movenames[6]
    $ movename8 = movenames[7]
    jump m1_1v1_turnb
    
label about_move(some_move):
    if (some_move == "Struggle"):
        "[[Power: 50 || Accuracy: 80 || Priority: -1 || Height: 0 || Physical || Normal || Close]\nA basic attack in which the user does absolutely whatever it can to harm the opponent. The flailing has a 25%% chance of causing self-damage equal to 25%% of damage done."
    if (some_move == "Pound"):
        "[[Power: 50 || Accuracy: 95 || Priority: 0 || Height: 0 || Physical || Normal || Close]\nA basic attack in which the user, with any blunt object (including fists) is used to strike the opponent."
    if (some_move == "Check"):
        "[[Power: 10 || Accuracy: 70 || Priority: 1 || Height: 0 || Physical || Normal || Close || Stun, 30]\nA somewhat advanced technique in which the user tries to get in a hit before the opponent. This has a 30%% chance of causing flinching."
    jump get_move_info
    
label movePenalty(mod1, mod2):
    if (curr_eval == "m1"):
        if (mod2 == "SP"):
            $ m1sp = m1sp + mod1
        if (mod2 == "FP"):
            $ m1fp = m1fp + mod1
        if (mod2 == "HP"):
            $ m1hp = m1hp + mod1
    if (curr_eval == "e1"):
        if (mod2 == "SP"):
            $ e1sp = e1sp + mod1
        if (mod2 == "FP"):
            $ e1fp = e1fp + mod1
        if (mod2 == "HP"):
            $ e1hp = e1hp + mod1
    return
            

label load_moves_part2:
    #this is for the AI
    if (eAIT == "firstfoe"):
        $ d20roll = renpy.random.randint(1, 20)
        if (d20roll < 5):
            $ chosenmove = "Check"
        else:
            $ chosenmove = "Pound"
    if(battle_current):
        call load_moves_part3(chosenmove)
    return
            
label load_moves_part3(chosenmove):        
    if (curr_eval == "m1"):
        $ cbm[chosenmove].assign("m1", chosenmove)
        $ curr_eval = "e1"
        call m1_damage_calc(m1power, m1accuracy, m1priority, m1parameter, m1parameterplus, m1typea, m1typeb)
        jump load_moves_part2
        
    if (curr_eval == "e1"):
        $ cbm[chosenmove].assign("e1", chosenmove)
        call e1_damage_calc(e1power, e1accuracy, e1priority, e1parameter, e1parameterplus, e1typea, e1typeb)
        jump a1v1_test