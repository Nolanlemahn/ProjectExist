screen combat_stats(cb1, cb2):
    $ show_combatant_stats(cb1, .02, .01)
    $ show_combatant_stats(cb2, .98, .01, False)

init 1 python:
    class Fight1v1:
        def __init__(self, combatant1, combatant2, firstStrike = None):
            store.showMCStatus = False
            self.combatant1 = combatant1
            self.combatant2 = combatant2
            self.firstTurn = True
            self.firstStrike = firstStrike
            self.evaluate = None
            self.complete = False
            self.messageAddon = ""
            self.message1 = ""
            self.message2 = ""
            self.conencted1 = False
            self.conencted2 = False
            self.damage1 = 0
            self.damage2 = 0
            self.combatWrapper()

        def combatWrapper(self):
            while not self.complete:
                # Check to see whose AI is checked first.
                self.turnProgress()
                # Grab the first person's choice
                self.turnManagement()
                # Grab the second person's choice
                self.otherEvaluation()
                # Actually try to deal damage
                self.dealDamage()
                # Prepare for the next turn
                self.reset()

        def reset(self):
            self.messageAddon = ""
            self.message1 = ""
            self.message2 = ""
            self.conencted1 = False
            self.conencted2 = False
            self.damage1 = 0
            self.damage2 = 0

        # see how we move to the next turn
        def turnProgress(self):
            c1priority = self.combatant1.movePriority
            c2priority = self.combatant2.movePriority
            c1speed = self.combatant1.speed
            c2speed = self.combatant2.speed

            def turnCheck(c1speed, c2speed):
                if(c1priority > c2priority):
                    evaluate = "c1"
                elif(c2priority > c1priority):
                    evaluate = "c2"
                # Priority said nothing, go by Combatant.speed
                else:
                    if(c1speed > c2speed):
                        evaluate = "c1"
                    else:#tie goes to the CPU
                        evaluate = "c2"
                return evaluate

            # If it's the first turn, check the story for who goes first
            if(self.firstTurn == True):
                if(self.firstStrike == "c1"):
                    self.evaluate = "c1"
                elif(self.firstStrike == "c2"):
                    self.evaluate = "c2"
                # Story says nothing, check the combat system (move priority 
                # or combatant speed)
                else:
                    self.evaluate = turnCheck(self.combatant1.speed, self.combatant2.speed)
            # If it isn't the first turn, check the combat system
            else:
                self.evaluate = turnCheck(self.combatant1.speed, self.combatant2.speed)


        def dealDamage(self):
            renpy.show_screen("combat_stats", self.combatant1, self.combatant2)
            c1priority = self.combatant1.movePriority
            c2priority = self.combatant2.movePriority
            c1speed = self.combatant1.speed
            c2speed = self.combatant2.speed

            if(self.firstTurn == True):
                self.firstTurn = False
                if(self.firstStrike == "c1"):
                    self.evaluate = "c1"
                elif(self.firstStrike == "c2"):
                    self.evaluate = "c2"
            else:
                if(c1priority > c2priority):
                    self.evaluate = "c1"
                elif(c2priority > c1priority):
                    self.evaluate = "c2"
                # Priority said nothing, go by Combatant.speed
                else:
                    if(c1speed > c2speed):
                        self.evaluate = "c1"
                    else:#tie goes to the CPU
                        self.evaluate = "c2"
            if(self.evaluate == "c1"):
                if(self.connected1):
                    self.combatant2.dealDamage(self.damage1)
                renpy.say(None, self.message1)
                if(self.connected2):
                    self.combatant1.dealDamage(self.damage2)
                renpy.say(None, self.message2)
            else:
                if(self.connected2):
                    self.combatant1.dealDamage(self.damage2)
                renpy.say(None, self.message2)
                if(self.connected1):
                    self.combatant2.dealDamage(self.damage1)
                renpy.say(None, self.message1)

        def turnManagement(self):
            if(self.evaluate == "c1"):
                attacker = self.combatant1
                defender = self.combatant2
            else:
                attacker = self.combatant2
                defender = self.combatant1

            if(attacker.AI == "Human"):
                self.humanRoutine(attacker.name)
            else:
                self.AIRoutine(attacker, defender)

        def otherEvaluation(self):
            if(self.evaluate == "c1"):
                self.evaluate = "c2" # other turn
                attacker = self.combatant2
                defender = self.combatant1
            else:
                self.evaluate = "c1" # other turn
                attacker = self.combatant1
                defender = self.combatant2

            if(attacker.AI == "Human"):
                self.humanRoutine(attacker.name)
            else:
                self.AIRoutine(attacker, defender)

        def humanRoutine(self, combatantName):
            chose = renpy.call_in_new_context("combat_choice_1", combatantName, self)
            if(chose == "fight"):
                chosenMove = self.moveSelection(combatantName)
                if(chosenMove == "None"):
                    self.humanRoutine(combatantName)
                else:
                    if(self.evaluate == "c1"):
                        attacker = self.combatant1
                        self.combatant1.movePriority = chosenMove.priority
                        defender = self.combatant2
                    else:
                        attacker = self.combatant2
                        self.combatant2.movePriority = chosenMove.priority
                        defender = self.combatant1
                    damage = self.calculateDamage(attacker, defender, chosenMove)
                    self.attemptDamage(attacker, defender, chosenMove, damage)

        def moveSelection(self, combatantName):
            chose = "None"
            while(chose == "None"):
                chose = renpy.call_in_new_context("load_moves_1", combatantName, self)
            return cbm[chose]

        def AIRoutine(self, attacker, defender):
            def AIMoveSelection():
                return aic[attacker.AI](attacker, defender)
            chosenMove = AIMoveSelection()
            if(self.evaluate == "c1"):
                attacker = self.combatant1
                self.combatant1.movePriority = chosenMove.priority
                defender = self.combatant2
            else:
                attacker = self.combatant2
                self.combatant2.movePriority = chosenMove.priority
                defender = self.combatant1
            damage = self.calculateDamage(attacker, defender, chosenMove)
            self.attemptDamage(attacker, defender, chosenMove, damage)

        def calculateDamage(self, attacker, defender, move):
            critdice = renpy.random.randint(0, 100)
            critmod = 1
            if(critdice <= 9):
                critmod = 2
                self.messageAddon = " It was a critical hit!"
            if(move.typea == "physical"):
                loadedAttack =  attacker.strength
                loadedDefense = defender.resistance
            elif(move.typea == "projectile"):
                loadedAttack =  attacker.dexterity
                loadedDefense = defender.resistance
            elif(move.typea == "aural"):
                loadedAttack =  attacker.intelligence
                loadedDefense = defender.spirit
            sect1 = (attacker.level * 2 / 5) + 2
            sect2 = (move.power)
            sect3 = (loadedAttack)
            sect4 = (loadedDefense)
            sect5 = 1

            battledice = renpy.random.randint(85, 100)
            
            damage = ((((((sect1 * sect2 * sect3 / 50) / sect4)) + 2) * critmod * battledice / 100) * sect5)
            if(self.evaluate == "c1"):
                self.damage1 = damage
            else:
                self.damage2 = damage

        def attemptDamage(self, attacker, defender, move, damage):
            hitdice = renpy.random.randint(0, 100)
            if(hitdice >= move.accuracy):
                message = attacker.name + " used " + move.name + "!" + self.messageAddon
                connected = True
            else:
                message = attacker.name + " used " + move.name + "!" + \
" But the attack missed..."
                connected = False
            if(self.evaluate == "c1"):
                self.message1 = message
                self.connected1 = connected 
            else:
                self.message2 = message
                self.connected2 = connected
            self.messageAddon = ""

label combat_choice_1(combatantName, combatInstance):
    show screen combat_stats(combatInstance.combatant1, combatInstance.combatant2)
    "What will [combatantName] do?{fast}{nw}"
    menu:
        extend "{fast}"
        "Fight":
            $ chose =  "fight"
        "Bag":
            $ chose = "inventory"
        "Switch":
            "There's no one to switch with...{fast}"
            $ chose =  "switch"
        "Run":
            "[combatantName] is not a coward and refuses to run!{fast}"
            $ chose =  "run"
    hide screen combat_stats
    return chose

label load_moves_1(combatantName, combatInstance):
    show screen combat_stats(combatInstance.combatant1, combatInstance.combatant2)
    if(combatInstance.evaluate == "c1"):
        $ evaluation = combatInstance.combatant1
    else:
        $ evaluation = combatInstance.combatant2
    $ chosenMove = "None"
    $ moveCount = 0
    $ moveNames = []
    $ moveCosts = []

    # Evaluate the moves
    python:
        for cb_move in evaluation.moves:
            moveNames.append(cb_move.name)
            moveCosts.append(cb_move.cost)
            moveCount += 1
        fakeCount = moveCount
        while (fakeCount < 6):
            moveNames.append("")
            fakeCount += 1

    $ movename1 = moveNames[0]
    $ movename2 = moveNames[1]
    $ movename3 = moveNames[2]
    $ movename4 = moveNames[3]
    $ movename5 = moveNames[4]
    $ movename6 = moveNames[5] 

    "Select a move to use.{fast}{nw}"
    menu:
        extend "{fast}"
        "%(movename1)s" if(moveCount > 0):
            $ chosenMove = movename1
        "%(movename2)s" if(moveCount > 1):
            $ chosenMove = movename2
        "%(movename3)s" if(moveCount > 2):
            $ chosenMove = movename3
        "%(movename4)s" if(moveCount > 3):
            $ chosenMove = movename4
        "%(movename5)s" if(moveCount > 4):
            $ chosenMove = movename5
        "%(movename6)s" if(moveCount > 5):
            $ chosenMove = movename6
        "(Get move information on known moves)":
            call get_move_info
        "(Do something else)":
            $ chosenMove = "Something Else"
    #if(battle_current):
    #    $ cbm[chosenmove].assign("m1", chosenmove)
    #    call load_moves_part3(chosenmove)
    hide screen combat_stats
    return chosenMove

label get_move_info:
    $ chosenMove = "None"
    "Which move would you like more information on?{fast}{nw}"
    menu:
        extend "{fast}"
        "%(movename1)s" if(moveCount > 0):
            $ chosenMove = movename1
        "%(movename2)s" if(moveCount > 1):
            $ chosenMove = movename2
        "%(movename3)s" if(moveCount > 2):
            $ chosenMove = movename3
        "%(movename4)s" if(moveCount > 3):
            $ chosenMove = movename4
        "%(movename5)s" if(moveCount > 4):
            $ chosenMove = movename5
        "%(movename6)s" if(moveCount > 5):
            $ chosenMove = movename6
        "(Done reading)":
            return
    call about_move(chosenMove)
    return

label about_move(some_move):
    # use the screen
    call screen move_details(cbm[some_move])
    #$ tempsay = cbm[some_move].asm_desc()
    #"[tempsay]"
    jump get_move_info
    return