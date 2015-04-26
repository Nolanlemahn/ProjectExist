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
            Show("combat_stats")
            self.combatWrapper()

        def combatWrapper(self):
            self.turnProgress()
            self.turnManagement()

        # see how we move to the next turn
        def turnProgress(self):
            c1priority = self.combatant1.movePriority
            c2priority = self.combatant2.movePriority

            def turnCheck(c1speed, c2speed):
                if (c1priority > c2priority):
                    evaluate = "c1"
                elif (c2priority > c1priority):
                    evaluate = "c2"
                # Priority said nothing, go by Combatant.speed
                else:
                    if (c1speed > c2speed):
                        evaluate = "c1"
                    else:#tie goes to the CPU
                        evaluate = "c2"
                return evaluate

            # If it's the first turn, check the story for who goes first
            if (self.firstTurn == True):
                self.firstTurn = False
                if (self.firstStrike == "c1"):
                    self.evaluate = "c1"
                elif (self.firstStrike == "c2"):
                    self.evaluate = "c2"
                # Story says nothing, check the combat system (move priority 
                # or combatant speed)
                else:
                    self.evaluate = turnCheck(self.combatant1.speed, self.combatant2.speed)
            # If it isn't the first turn, check the combat system
            else:
                self.evaluate = turnCheck(self.combatant1.speed, self.combatant2.speed)

        def turnManagement(self):
            if(self.evaluate == "c1"):
                evaluation = self.combatant1
            else:
                evaluation = self.combatant2

            if(evaluation.AI == "Human"):
                self.humanRoutine(evaluation.name)
            else:
                self.AIRoutine()

        def humanRoutine(self, combatantName):
            chose = renpy.call_in_new_context("combat_choice_1", combatantName, self)
            if(chose == "fight"):
                chosenMove = self.moveSelection(combatantName)

        def moveSelection(self, combatantName):
            chose = "None"
            while(chose == "None"):
                chose = renpy.call_in_new_context("load_moves_1", combatantName, self)
            return cbm[chose]

        def AIRoutine(self):
            return

        def calculateDamage(self, attacker, defender, move):
            return

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
        "%(movename1)s" if (moveCount > 0):
            $ chosenMove = movename1
        "%(movename2)s" if (moveCount > 1):
            $ chosenMove = movename2
        "%(movename3)s" if (moveCount > 2):
            $ chosenMove = movename3
        "%(movename4)s" if (moveCount > 3):
            $ chosenMove = movename4
        "%(movename5)s" if (moveCount > 4):
            $ chosenMove = movename5
        "%(movename6)s" if (moveCount > 5):
            $ chosenMove = movename6
        "(Get move information on known moves)":
            call get_move_info
        "(Do something else)":
            jump m1_1v1_turna
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
        "%(movename1)s" if (moveCount > 0):
            $ chosenMove = movename1
        "%(movename2)s" if (moveCount > 1):
            $ chosenMove = movename2
        "%(movename3)s" if (moveCount > 2):
            $ chosenMove = movename3
        "%(movename4)s" if (moveCount > 3):
            $ chosenMove = movename4
        "%(movename5)s" if (moveCount > 4):
            $ chosenMove = movename5
        "%(movename6)s" if (moveCount > 5):
            $ chosenMove = movename6
        "(Do something else)":
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