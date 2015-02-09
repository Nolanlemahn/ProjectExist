label battle_end:
    $ single_combat_check = True
    "It's over..."
    $ fight_is_1v1 = False
    $ battle_current = False
    #if (progress == "001")
    return

label battle_death:
    $ single_combat_check = True
    "It's over..."
    $ battle_current = False
    return
    
label about_move(some_move):
    # use the screen
    call screen move_details(cbm[some_move])
    #$ tempsay = cbm[some_move].asm_desc()
    #"[tempsay]"
    jump get_move_info
    return
    
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
        $ cbm[chosenmove].assign("e1", chosenmove)
        call load_moves_part3(chosenmove)
    return
            
label load_moves_part3(chosenmove):
    if (curr_eval == "m1"):
        $ curr_eval = "e1"
        call m1_damage_calc(m1power, m1accuracy, m1priority, m1parameter, m1parameterplus, m1typea, m1typeb)
        jump load_moves_part2
        
    if (curr_eval == "e1"):
        call e1_damage_calc(e1power, e1accuracy, e1priority, e1parameter, e1parameterplus, e1typea, e1typeb)
        jump a1v1_test