label battle_end:
    $ single_combat_check = True
    "It's over..."
    #if (progress == "001")

label battle_death:
    $ single_combat_check = True
    "It's over..."

label load_moves_part1(moveset):#player1
    $ movecount = 0
    $ moveexists = 0
    while (movecount < 8):
        if (moveset[movecount] == 0):
            $ movenames[movecount] = "DNE"
        if (moveset[movecount] == 1):
            $ moveexists = moveexists + 1
            $ movenames[movecount] = "Pound"
            $ movecosts[2 * movecount] = ""
            $ movecosts[2 * movecount + 1] = ""
        if (moveset[movecount] == 2):
            $ moveexists = moveexists + 1
            $ movenames[movecount] = "Check"
            $ movecosts[2 * movecount] = ""
            $ movecosts[2 * movecount + 1] = ""
        
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
    call load_moves_part3(chosenmove)
            
label load_moves_part3(chosenmove):
    if (chosenmove == "Struggle"):
        $ power = 50
        $ accuracy = 0.80
        $ prority = 0
        $ parameter = "struggle"
        $ typea = "physical"
        $ typeb = "normal"
        $ typec = "close"
        $ cost = ["", ""]
    
    if (chosenmove == "Pound"):
        $ power = 50
        $ accuracy = 0.95
        $ priority = 0
        $ parameter = "null"
        $ typea = "physical"
        $ typeb = "normal"
        $ typec = "close"
        $ cost = ["", ""]
        
    if (chosenmove == "Check"):
        $ power = 10
        $ accuracy = 0.70
        $ priority = 1
        $ parameter = "stun"
        $ parameterplus = 30
        $ typea = "physical"
        $ typeb = "normal"
        $ typec = "close"
        $ cost = ["", ""]
        
    if (chosenmove == "Warlock's Fist"):
        $ power = 85
        $ accuracy = 100
        $ priority = -1
        $ parameter = "homing"
        $ typea = "physical"
        $ typeb = "dream"
        $ typec = "close"
        $ cost = [-4, "SP"]
        
    if (curr_eval == "m1"):
        $ m1power = power
        $ m1accuracy = accuracy
        $ m1priority = priority
        $ m1move = chosenmove
        $ m1parameter = parameter
        $ m1parameterplus = parameterplus
        $ m1cost = cost[:]
        $ curr_eval = "e1"
        call m1_damage_calc(power, accuracy, priority, parameter, parameterplus, typea, typeb)
        
    if (curr_eval == "e1"):
        $ e1power = power
        $ e1accuracy = accuracy
        $ e1priority = priority
        $ e1move = chosenmove
        $ e1parameter = parameter
        $ e1parameterplus = parameterplus
        $ e1cost = cost[:]
        #"hold up"
        call e1_damage_calc(power, accuracy, priority, parameter, parameterplus, typea, typeb)