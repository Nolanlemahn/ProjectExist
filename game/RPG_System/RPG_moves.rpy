#######
# File name: RPG_moves.rpy
# 
# Description: Implements a dclass for hollding RPG moves.
# 
# Original author: Nolan/NintendoToad
# 
# Type: Library
# Usage:
#     Don't directly use this, but regularly update cbm
#######

init:
    $ cbm = collections.OrderedDict()
    # 0
    $ cbm["Struggle"] = cb_move(50, 0.80, 0, "struggle", None, "physical", "normal", "close", ["", ""])
    # 1-3
    $ cbm["Pound"] = cb_move(50, 0.95, 0, "null", None, "physical", "normal", "close", ["", ""])
    $ cbm["Check"] = cb_move(10, 0.70, 1, "stun", 30, "physical", "normal", "close", ["", ""])
    $ cbm["Warlock's Fist"] = cb_move(85, 1.00, -1, "homing", None, "physical", "dream", "close", [-4, "SP"])
    
    $ cbm["Pound"].desc = "A basic attack in which the user, with any blunt object (including fists), strikes the opponent."
    $ cbm["Check"].desc = "A somewhat advanced technique in which the user tries to get in a hit before the opponent. This has a 30%% chance of causing flinching."
    $ cbm["Warlock's Fist"].desc = "A somewhat advanced technique that requires use of tactics learned in Dream Worlds. The user locks onto his opponent's being, and launches a strong punch backed with Dream Energy"

init -1 python:
    #####
    # Class name: cb_move()
    # 
    # Descripiton: Define moves for combat.
    # 
    # Parameters:
    # power - the base power of the move
    # accuracy - move's base chance to hit
    # prority - speed of the move
    # parameter - special parameter
    # parameterplus - special parameter
    # typea - physical or projectile?
    # typeb - element
    # typec - when I know what this does I'll tell you
    # cost - the cost to use
    # the really long text
    #
    # Returns: a move object of sorts
    #####
    class cb_move:

        def __init__(self, power, accuracy, priority, parameter, parameterplus, typea, typeb, typec, cost, desc = ""):
            self.power = power
            self.accuracy = accuracy
            self.priority = priority
            self.parameter = parameter
            self.parameterplus = parameterplus
            self.typea = typea
            self.typeb = typeb
            self.typec = typec
            self.cost = cost
            self.desc = desc
        def assign(move, user, movename):
            if(user == "m1"):
                store.m1power = move.power
                store.m1accuracy = move.accuracy
                store.m1priority = move.priority
                store.m1move = movename
                store.m1parameter = move.parameter
                store.m1parameterplus = move.parameterplus
                store.m1typea = move.typea
                store.m1typeb = move.typeb
                store.m1typec = move.typec
                store.m1cost = move.cost[:]
            elif(user == "e1"):
                store.e1power = move.power
                store.e1accuracy = move.accuracy
                store.e1priority = move.priority
                store.e1move = movename
                store.e1parameter = move.parameter
                store.e1parameterplus = move.parameterplus
                store.e1typea = move.typea
                store.e1typeb = move.typeb
                store.e1typec = move.typec
                store.e1cost = move.cost[:]