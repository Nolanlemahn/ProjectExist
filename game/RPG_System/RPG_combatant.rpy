init python:
    
    #####
    # Class name: combatant()
    # 
    # Description: A class for someone that can get into a fight.
    # 
    # Parameters:
    #
    #####
    class Combatant:
        def __init__(self, name, LVL, STR, DEX, RES, SPD, INT, SPI, maxHP, maxXP,
                     maxSleep, maxBelly, Ability1, Ability1Level, Ability2, 
                     Ability2Level, Symbol1, Symbol1Level, Symbol2, Symbol2Level, 
                     Weapon, Armor, KnownMoves, AI = "Test", Default = True,
                     currHP = -1, currXP = -1, currBelly = -1, currSleep = -1):
            self.name = name
            self.level = LVL
            self.strength = STR #determines damage with physical attacks
            self.dexterity = DEX #determines damage with ranged attacks
            self.resistance = RES #determines resistance against physical/projectile attacks
            self.speed = SPD #partially determines priority in move order
            self.intelligence = INT #determines damage with aural attacks
            self.spirit = SPI # determines resistance against aural attacks
            self.maxHP = maxHP
            self.maxXP = maxXP
            self.maxSleep = maxSleep
            self.maxBelly = maxBelly
            self.ability1 = cb_ability(Ability1, Ability1Level)
            self.ability2 = cb_ability(Ability2, Ability2Level)
            self.symbol1 = cb_ability(Symbol1, Symbol1Level)
            self.symbol2 = cb_ability(Symbol2, Symbol2Level)
            self.weapon = Weapon
            self.armor = Armor
            self.inventory = [] # eventually sort
            self.lookupMoves(KnownMoves)
            self.AI = AI
            self.movePriority = 0
            self.isMoving = True
            self.KOd = True
            self.status = []
            self.setState(currHP, currXP, currBelly, currSleep, Default)

        def setState(self, HP = -1, XP = -1, Sleep = -1, Belly = -1, default = False):
            # default case
            if(default == True):
                self.currentHP = self.maxHP
                self.currentXP = 0
                self.currentSleep = self.maxSleep
                self.currentBelly = self.maxBelly
                return
            # explicit case
            self.currentHP = HP
            self.currentXP = XP
            self.currentSleep = Sleep
            self.currentBelly = Belly
            return

        def doChange(self, passedvar, passedvalue):
            if(passedvar == "HP"):
                self.currentHP += passedvalue
            elif(passedvar == "FP"):
                self.currentBelly += passedvalue
            elif(passedvar == "SP"):
                self.currentSleep += passedvalue
            self.checkUp()

        def evaluateStatus(self):
            self = self.statusChain()

        def statusChain(self):
            copy = self
            index = 0
            for condition in copy.status:
                 copy = after_cbe[condition[0]](copy)
            for condition in copy.status:
                 copy.status[index][1] -= 1
            copy.checkUp()
            return copy

        def checkUp(self):
            knockedout = False
            removed = False
            if(self.currentHP < 0):
                self.currentHP = 0
                knockedout = True
            if(self.currentBelly < 0):
                self.currentBelly = 0
                knockedout = True
            if(self.currentSleep < 0):
                self.currentSleep = 0
                knockedout = True
            self.KOd = knockedout
            for condition in self.status:
                if(removed):
                    self.checkUp()
                    return
                if(condition[1] <= 0):
                    self.status.remove(condition)
                    removed = True

        def dealDamage(self, damage):
            self.doChange("HP", damage * -1)

        def inflictStatus(self, status):
            self.status.append(status)

        def lookupMoves(self, KnownMoves):
            actualMoves = []
            movesCount = 0
            # these are expected to be Strings
            # YES, we want to make copies. Bosses will be using stronger 
            # versions of specific moves. For instance, Rin's Warlock Punch
            # will have more power than anyone else's.
            for cb_m in KnownMoves:
                if cb_m in store.cbm:
                    movesCount += 1
                    actualMoves.append(store.cbm[cb_m])
                else:
                    renpy.error("Move not defined (in store.cbm): %s. Perhaps \
                                 you should double-check RPG_moves.rpy?" % cb_m)
            self.moves = actualMoves
            return

        def evaluateAbilities(self):
            return

        def addMove(self):
            return

        def manualAddMove(self):
            return


