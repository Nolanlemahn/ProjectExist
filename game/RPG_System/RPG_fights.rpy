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
            #while(self.complete == False):
            show_combatant_stats(self.combatant1, .02, .01)
            show_combatant_stats(self.combatant2, .98, .01, False)
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
            chose = renpy.call("combat_choice_1", combatantName, self)
            return

        def moveSelection(self):
            return

        def AIRoutine(self):
            return

label combat_choice_1(combatant_name, combatInstance):
    show screen combat_stats(combatInstance.combatant1, combatInstance.combatant2)
    "What will [combatant_name] do?{fast}{nw}"
    menu:
        extend "{fast}"
        "Fight":
            return "fight"
        "Bag":
            return "inventory"
        "Switch":
            "There's no one to switch with...{fast}"
            return "switch"
        "Run":
            "[m1name] is not a coward and refuses to run!{fast}"
            return "run"
    return