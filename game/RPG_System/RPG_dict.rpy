init python:
    import collections #OrderedDict()

init:
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

    $ aic = collections.OrderedDict()
    $ aic["Test"] = AIForTestEnemy

init -1 python:
    def AIForTestEnemy(attacker, defender):
        return cbm["Warlock's Fist"]
