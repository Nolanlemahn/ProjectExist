label a1v1_test:
    if (firstturn == True):
        $ firstturn = False
        if (precursor == "m1"):
            $ curr_eval = "m1"
        elif (precursor == "e1"):
            $ curr_eval = "e1"
        else:
            if (m1priority > e1priority):
                $ curr_eval = "m1"
            elif (e1priority > m1priority):
                $ curr_eval = "m1"
            else:
                if (m1stats[3] > e1SPD):
                    $ curr_eval = "m1"
                else:#tie goes to the CPU
                    $ curr_eval = "e1"
    else:
        if (m1priority > e1priority):
            $ curr_eval = "m1"
        elif (e1priority > m1priority):
            $ curr_eval = "m1"
        else:
            if (m1stats[3] > e1SPD):
                $ curr_eval = "m1"
            else:#tie goes to the CPU
                $ curr_eval = "e1"
    jump deal_damage
        
        
label deal_damage:
    $ m1pass = True
    $ e1pass = True
    if (curr_eval == "m1"):
        #-status-#
        if (m1status == "stunned"):
            $ m1mess2 = check_status("m1")
            $ m1mess2 = m1mess2[1]
            "[m1name][m1mess2]{fast}"
            $ m1pass = False
        #-accuracy-#
        $ probability = m1accuracy
        $ hitdice = renpy.random.randint(0, 100)
        if ((m1pass == True) and (hitdice > (probability * 100))):
            call movePenalty(m1cost[0], m1cost[1])
            "[m1name] used [m1move]! But the attack missed...{fast}"
        #-damage-#
        elif (m1pass == True):
            call movePenalty(m1cost[0], m1cost[1])
            "[m1name] used [m1move]![m1mess1]{fast}"
            with vpunch
            $ e1hp = e1hp - m1damage
            if (m1parameter == "stun"):
                $ m1statdice = renpy.random.randint(0, 100)
                if (m1statdice < m1parameterplus):
                    $ e1status = "stunned"
                    "[e1name] was stunned by the [m1move]!{fast}"
         
        $ curr_eval = "e1"
        #-status-#
        if (e1status == "stunned"):
            $ e1mess2 = check_status("e1")
            $ e1mess2 = e1mess2[1]
            "[e1name][e1mess2]"
            $ e1pass = False
        #-accuracy-#
        $ probability = e1accuracy
        $ hitdice = renpy.random.randint(0, 100)
        if (hitdice > (probability * 100)):
            $ e1pass = False
            "[e1name] used [e1move]! But the attack missed...{fast}"
        #-damage-#
        if (e1pass == True):
            "[e1name] used [e1move]![e1mess1]{fast}"
            with vpunch
            $ m1hp = m1hp - e1damage
            call domchange("HP", -1 * e1damage, 1)
            if (e1parameter == "stun"):
                $ e1statdice = renpy.random.randint(0, 100)
                if (e1statdice < e1parameterplus):
                    $ m1status = "stunned"
                    "[m1name] was stunned by the [e1move]!{fast}"
        $ curr_eval = "m1"
                    
    else:
        #-status-#
        if (e1status == "stunned"):
            $ e1mess2 = check_status("e1")
            $ e1mess2 = e1mess2[1]
            "[e1name][e1mess2]"
            $ e1pass = False
        #-accuracy-#
        $ probability = e1accuracy
        $ hitdice = renpy.random.randint(0, 100)
        if (hitdice > (probability * 100)):
            $ e1pass = False
            "[e1name] used [e1move]! But the attack missed...{fast}"
        #-damage-#
        if (e1pass == True):
            "[e1name] used [e1move]![e1mess1]"
            with vpunch
            $ m1hp = m1hp - e1damage
            call domchange("HP", -1 * e1damage, 1)
            if (e1parameter == "stun"):
                $ e1statdice = renpy.random.randint(0, 100)
                if (e1statdice < e1parameterplus):
                    $ m1status = "stunned"
                    "[m1name] was stunned by the [e1move]!{fast}"
        
        $ curr_eval = "m1"
        #-status-#
        if (m1status == "stunned"):
            $ m1mess2 = check_status("m1")
            $ m1mess2 = m1mess2[1]
            "[m1name][m1mess2]{fast}"
            $ m1pass = False
        #-accuracy-#
        $ probability = m1accuracy
        $ hitdice = renpy.random.randint(0, 100)
        if ((m1pass == True) and (hitdice > (probability * 100))):
            call movePenalty(m1cost[0], m1cost[1])
            "[m1name] used [m1move]! But the attack missed...{fast}"
        #-damage-#
        elif (m1pass == True):
            call movePenalty(m1cost[0], m1cost[1])
            "[m1name] used [m1move]![m1mess1]{fast}"
            with vpunch
            $ e1hp = e1hp - m1damage
            if (m1parameter == "stun"):
                $ m1statdice = renpy.random.randint(0, 100)
                if (m1statdice < m1parameterplus):
                    $ e1status = "stunned"
                    "[e1name] was stunned by the [m1move]!{fast}"
        $ curr_eval = "e1"
    jump m1_1v1_turnb
   
label m1_damage_calc(po, ac, pr, pa, pp, ta, tb):
    #call m1_damage_calc(power, accuracy, priority, parameter, parameterplus, typea, typeb)
    #is it a crit
    $ critdice = renpy.random.randint(0, 100)
    if (critdice < 9):
        $ critmod = 2
        $ m1mess1 = " It was a critical hit!"
    else:
        $ critmod = 1
        $ m1mess1 = ""
        
    #check the parameter, bitch
        
    if (ta == "physical"):
        $ helphand = 1 #1v1 battle, no such thing as helping hand, 1.5 if assistance is present
        $ itemmult1 = 1 #be safe, test for items after this line resetting itemmult (base power only)
        $ itemmult2 = 1 #be safe, test for items (items that change the stat)
        $ nextboost = 1 #be safe, test for the last used move after this line resetting nextboost
        $ field1 = 1 #field bonus day/night
        $ field2 = 1 #field bonus air (sandstorm, high winds, rain)
        $ field3 = 1 #field bonus ground
        $ m1ability1 = 1 #ability bonus, changes base power (double base power under 60, etc)
        $ m1ability2 = 1 #ability bonus, changes stats
        $ e1ability = 1 #ability subtraction
        $ m1statm = 1 #stat multiplier
        $ e1statm = 1 #stat divider
        $ explode = 1 #big boom divider
        $ burn = 1 #0.5 or 1
        
        $ sect1 = (m1level * 2 / 5) + 2
        $ sect2 = (helphand * po * itemmult1 * nextboost * field1 * field2 * m1ability1 * e1ability)
        $ sect3 = (m1stats[0] * m1statm * m1ability2 * itemmult2)
        $ sect4 = (e1RES * e1statm * explode)
        $ sect5 = 1#this will eventually be STAB and typing

        # Mod2
        ## Item modifier AND/OR [me first] move
        # R = a random number between 85 and 100 (that is, 100-rand(0,15)
        $ battledice = renpy.random.randint(85, 100)
        
        # STAB
        # Type1
        # Type2
        # Mod3 = SRF × EB × TL × TRB
        ## SRF: solid rock or filter, EB expert belt, TL tinted lens, TRB type-resisting berry
        
        #"Test [po] [ac] [parameter]"
        $ damage = ((((((sect1 * sect2 * sect3 / 50) / sect4) * burn * field3) + 2) * critmod * battledice / 100) * sect5)
        
    elif (ta == "aural"):
        $ helphand = 1 #1v1 battle, no such thing as helping hand, 1.5 if assistance is present
        $ itemmult1 = 1 #be safe, test for items after this line resetting itemmult (base power only)
        $ itemmult2 = 1 #be safe, test for items (items that change the stat)
        $ nextboost = 1 #be safe, test for the last used move after this line resetting nextboost
        $ field1 = 1 #field bonus day/night
        $ field2 = 1 #field bonus air (sandstorm, high winds, rain)
        $ field3 = 1 #field bonus ground
        $ m1ability1 = 1 #ability bonus, changes base power (double base power under 60, etc)
        $ m1ability2 = 1 #ability bonus, changes stats
        $ e1ability = 1 #ability subtraction
        $ m1statm = 1 #stat multiplier
        $ e1statm = 1 #stat divider
        $ explode = 1 #big boom divider
        $ burn = 1 #this is never 0.5
        
        $ sect1 = (m1level * 2 / 5) + 2
        $ sect2 = (helphand * po * itemmult1 * nextboost * field1 * field2 * m1ability1 * e1ability)
        $ sect3 = (m1stats[4] * m1statm * m1ability2 * itemmult2)
        $ sect4 = (e1SPI * e1statm * explode)
        $ sect5 = 1#this will eventually be STAB and typing

        # Mod2
        ## Item modifier AND/OR [me first] move
        # R = a random number between 85 and 100 (that is, 100-rand(0,15)
        $ battledice = renpy.random.randint(85, 100)
        
        # STAB
        # Type1
        # Type2
        # Mod3 = SRF × EB × TL × TRB
        ## SRF: solid rock or filter, EB expert belt, TL tinted lens, TRB type-resisting berry
        
        #"Test [po] [ac] [parameter]"
        $ damage = ((((((sect1 * sect2 * sect3 / 50) / sect4) * burn * field3) + 2) * critmod * battledice / 100) * sect5)
        
    elif (ta == "projectile"):
        $ helphand = 1 #1v1 battle, no such thing as helping hand, 1.5 if assistance is present
        $ itemmult1 = 1 #be safe, test for items after this line resetting itemmult (base power only)
        $ itemmult2 = 1 #be safe, test for items (items that change the stat)
        $ nextboost = 1 #be safe, test for the last used move after this line resetting nextboost
        $ field1 = 1 #field bonus day/night
        $ field2 = 1 #field bonus air (sandstorm, high winds, rain)
        $ field3 = 1 #field bonus ground
        $ m1ability1 = 1 #ability bonus, changes base power (double base power under 60, etc)
        $ m1ability2 = 1 #ability bonus, changes stats
        $ e1ability = 1 #ability subtraction
        $ m1statm = 1 #stat multiplier
        $ e1statm = 1 #stat divider
        $ explode = 1 #big boom divider
        $ burn = 1 #this is never 0.5
        
        $ sect1 = (m1level * 2 / 5) + 2
        $ sect2 = (helphand * po * itemmult1 * nextboost * field1 * field2 * m1ability1 * e1ability)
        $ sect3 = (m1stats[1] * m1statm * m1ability2 * itemmult2)
        $ sect4 = (e1RES * e1statm * explode)
        $ sect5 = 1#this will eventually be STAB and typing

        # Mod2
        ## Item modifier AND/OR [me first] move
        # R = a random number between 85 and 100 (that is, 100-rand(0,15)
        $ battledice = renpy.random.randint(85, 100)
        
        # STAB
        # Type1
        # Type2
        # Mod3 = SRF × EB × TL × TRB
        ## SRF: solid rock or filter, EB expert belt, TL tinted lens, TRB type-resisting berry
        
        #"Test [po] [ac] [parameter]"
        $ damage = ((((((sect1 * sect2 * sect3 / 50) / sect4) * burn * field3) + 2) * critmod * battledice / 100) * sect5)
    
    $ m1damage = damage
    jump load_moves_part2
    
 
label e1_damage_calc(po, ac, pr, pa, pp, ta, tb):
    #is it a crit
    $ critdice = renpy.random.randint(0, 100)
    if (critdice < 9):
        $ critmod = 2
        $ e1mess1 = " It was a critical hit!"
    else:
        $ critmod = 1
        $ e1mess1 = ""
        
    #check the parameter, bitch
        
    if (ta == "physical"):
        $ helphand = 1 #1v1 battle, no such thing as helping hand, 1.5 if assistance is present
        $ itemmult1 = 1 #be safe, test for items after this line resetting itemmult (base power only)
        $ itemmult2 = 1 #be safe, test for items (items that change the stat)
        $ nextboost = 1 #be safe, test for the last used move after this line resetting nextboost
        $ field1 = 1 #field bonus day/night
        $ field2 = 1 #field bonus air (sandstorm, high winds, rain)
        $ field3 = 1 #field bonus ground
        $ e1ability1 = 1 #ability bonus, changes base power (double base power under 60, etc)
        $ e1ability2 = 1 #ability bonus, changes stats
        $ m1ability = 1 #ability subtraction
        $ e1statm = 1 #stat multiplier
        $ m1statm = 1 #stat divider
        $ explode = 1 #big boom divider
        $ burn = 1 #0.5 or 1
        
        $ sect1 = (e1level * 2 / 5) + 2
        $ sect2 = (helphand * po * itemmult1 * nextboost * field1 * field2 * e1ability1 * m1ability)
        $ sect3 = (e1STR * e1statm * e1ability2 * itemmult2)
        $ sect4 = (m1stats[2] * m1statm * explode)
        $ sect5 = 1#this will eventually be STAB and typing

        # Mod2
        ## Item modifier AND/OR [me first] move
        # R = a random number between 85 and 100 (that is, 100-rand(0,15)
        $ battledice = renpy.random.randint(85, 100)
        
        # STAB
        # Type1
        # Type2
        # Mod3 = SRF × EB × TL × TRB
        ## SRF: solid rock or filter, EB expert belt, TL tinted lens, TRB type-resisting berry
        
        #"Test [po] [ac] [parameter]"
        $ damage = ((((((sect1 * sect2 * sect3 / 50) / sect4) * burn * field3) + 2) * critmod * battledice / 100) * sect5)
        
    elif (ta == "aural"):
        $ helphand = 1 #1v1 battle, no such thing as helping hand, 1.5 if assistance is present
        $ itemmult1 = 1 #be safe, test for items after this line resetting itemmult (base power only)
        $ itemmult2 = 1 #be safe, test for items (items that change the stat)
        $ nextboost = 1 #be safe, test for the last used move after this line resetting nextboost
        $ field1 = 1 #field bonus day/night
        $ field2 = 1 #field bonus air (sandstorm, high winds, rain)
        $ field3 = 1 #field bonus ground
        $ e1ability1 = 1 #ability bonus, changes base power (double base power under 60, etc)
        $ e1ability2 = 1 #ability bonus, changes stats
        $ m1ability = 1 #ability subtraction
        $ e1statm = 1 #stat multiplier
        $ m1statm = 1 #stat divider
        $ explode = 1 #big boom divider
        $ burn = 1 #this is never 0.5
        
        $ sect1 = (e1level * 2 / 5) + 2
        $ sect2 = (helphand * po * itemmult1 * nextboost * field1 * field2 * e1ability1 * m1ability)
        $ sect3 = (e1INT * e1statm * e1ability2 * itemmult2)
        $ sect4 = (m1stats[5] * m1statm * explode)
        $ sect5 = 1#this will eventually be STAB and typing

        # Mod2
        ## Item modifier AND/OR [me first] move
        # R = a random number between 85 and 100 (that is, 100-rand(0,15)
        $ battledice = renpy.random.randint(85, 100)
        
        # STAB
        # Type1
        # Type2
        # Mod3 = SRF × EB × TL × TRB
        ## SRF: solid rock or filter, EB expert belt, TL tinted lens, TRB type-resisting berry
        
        #"Test [po] [ac] [parameter]"
        $ damage = ((((((sect1 * sect2 * sect3 / 50) / sect4) * burn * field3) + 2) * critmod * battledice / 100) * sect5)
        
    elif (ta == "projectile"):
        $ helphand = 1 #1v1 battle, no such thing as helping hand, 1.5 if assistance is present
        $ itemmult1 = 1 #be safe, test for items after this line resetting itemmult (base power only)
        $ itemmult2 = 1 #be safe, test for items (items that change the stat)
        $ nextboost = 1 #be safe, test for the last used move after this line resetting nextboost
        $ field1 = 1 #field bonus day/night
        $ field2 = 1 #field bonus air (sandstorm, high winds, rain)
        $ field3 = 1 #field bonus ground
        $ e1ability1 = 1 #ability bonus, changes base power (double base power under 60, etc)
        $ e1ability2 = 1 #ability bonus, changes stats
        $ m1ability = 1 #ability subtraction
        $ e1statm = 1 #stat multiplier
        $ m1statm = 1 #stat divider
        $ explode = 1 #big boom divider
        $ burn = 1 #this is never 0.5
        
        $ sect1 = (e1level * 2 / 5) + 2
        $ sect2 = (helphand * po * itemmult1 * nextboost * field1 * field2 * e1ability1 * m1ability)
        $ sect3 = (e1DEX * e1statm * e1ability2 * itemmult2)
        $ sect4 = (m1stats[2] * m1statm * explode)
        $ sect5 = 1#this will eventually be STAB and typing

        # Mod2
        ## Item modifier AND/OR [me first] move
        # R = a random number between 85 and 100 (that is, 100-rand(0,15)
        $ battledice = renpy.random.randint(85, 100)
        
        # STAB
        # Type1
        # Type2
        # Mod3 = SRF × EB × TL × TRB
        ## SRF: solid rock or filter, EB expert belt, TL tinted lens, TRB type-resisting berry
        
        #"Test [po] [ac] [parameter]"
        $ damage = ((((((sect1 * sect2 * sect3 / 50) / sect4) * burn * field3) + 2) * critmod * battledice / 100) * sect5)
        
    $ e1damage = damage
    $ batcheckpoint = 1
    jump a1v1_test