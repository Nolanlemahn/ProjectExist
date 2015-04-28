label combat_test:
    scene bg blackdrop
    $ main_char = Combatant("Kazuki", 5, 11, 11, 20, 14, 14, 20, 100, 50, 100, 
                          100, None, 0, None, 0, None, 0, None, 0, "Fists", 
                          "Nothing", ["Pound", "Check"], "Human")
    $ bully = Combatant("Test", 5, 11, 11, 20, 14, 14, 20, 100, 50, 100, 
                        100, None, 0, None, 0, None, 0, None, 0, "Fists", 
                        "Nothing", ["Pound", "Check"], "Test")
    $ fightInstance = Fight1v1(main_char, bully, "c1")
    $ main_char, bully = fightInstance.process()
    "Test"