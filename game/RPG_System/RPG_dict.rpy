init python:
    import collections #OrderedDict()

init:
    # Combat moves go here.
    $ cbm = collections.OrderedDict()
    # 0
    $ cbm["Struggle"] = cb_move("Struggle", 50, 0.80, 0, "struggle", None, "physical", "normal", "close", ["", ""])
    # 1-3
    $ cbm["Pound"] = cb_move("Pound", 50, 0.95, 0, None, None, "physical", "normal", "close", ["", ""])
    $ cbm["Check"] = cb_move("Check", 10, 0.70, 1, "stun", 30, "physical", "normal", "close", ["", ""])
    $ cbm["Warlock's Fist"] = cb_move("Warlock's Fist", 85, 1.00, -1, "homing", None, "physical", "dream", "close", [-4, "SP"])
    $ cbm["Something Else"] = "None"

    $ cbm["Pound"].desc = "A basic attack in which the user, with any blunt object (including fists), strikes the opponent."
    $ cbm["Check"].desc = "A somewhat advanced technique in which the user tries to get in a light but surprising hit before the opponent has time to react. This has a 30% chance of causing flinching."
    $ cbm["Warlock's Fist"].desc = "A somewhat advanced technique that requires use of tactics learned in Dream Worlds. The user locks onto his opponent's mind, and launches a strong punch backed with Dream Energy."
    ###

    # AI for Combatants
    $ aic = dict()
    $ aic["Test"] = AIForTestEnemy

    #Effects
    $ cbe = dict()
    $ after_cbe = dict()

    $ cbe["stun"] = stunningMove
    $ after_cbe["stunned"] = isStunned

init -1 python:
    # AI Functions go here
    def AIForTestEnemy(attacker, defender):
        return cbm["Warlock's Fist"]

    #Effect handler functions
    def stunningMove(attacker, defender, cbmove):
        chancedice = renpy.random.randint(0, 100)
        if(chancedice < cbmove.parameterplus):
            renpy.say(None, defender.name + " was stunned!")
            status = ["stunned", 1]
            defender.inflictStatus(status)
        return defender

    def isStunned(combatant):
        renpy.say(None, combatant.name + " is stunned and unable to move!")
        combatant.isMoving = False
        return combatant

