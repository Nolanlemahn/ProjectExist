init 1 python:
    class Fight1v1:
        def __init__(self, combatant1, combatant2, firstStrike = None):
            self.combatant1 = combatant1
            self.combatant2 = combatant2
            self.firstTurn = True
            self.firstStrike = firstStrike
            self.evaluate = None
            self.turnProgress()

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
