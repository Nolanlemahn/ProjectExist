init -1:
    $ athenaGloss = file(config.gamedir + "/glossary/characters/athenagloss.txt").read().decode("utf-8")
    $ jonGloss = file(config.gamedir + "/glossary/characters/jongloss.txt").read().decode("utf-8")
    $ kazukiGloss = file(config.gamedir + "/glossary/characters/kazukigloss.txt").read().decode("utf-8")
    $ lawGloss = file(config.gamedir + "/glossary/characters/lawgloss.txt").read().decode("utf-8")
    $ masaGloss = file(config.gamedir + "/glossary/characters/masagloss.txt").read().decode("utf-8")
    $ natGloss = file(config.gamedir + "/glossary/characters/natgloss.txt").read().decode("utf-8")
    $ rinGloss = file(config.gamedir + "/glossary/characters/ringloss.txt").read().decode("utf-8")
    $ tammyGloss = file(config.gamedir + "/glossary/characters/tammygloss.txt").read().decode("utf-8")
    $ ult7Gloss1 = file(config.gamedir + "/glossary/characters/ult7gloss1.txt").read().decode("utf-8")
    $ ult7Gloss2 = file(config.gamedir + "/glossary/characters/ult7gloss2.txt").read().decode("utf-8")
    $ ult7Gloss3 = file(config.gamedir + "/glossary/characters/ult7gloss3.txt").read().decode("utf-8")
    $ liliGloss = file(config.gamedir + "/glossary/characters/liligloss.txt").read().decode("utf-8")
    
label about_fp:
    scene bg mainmenu
    "FP/Food Points serves as your hunger and in some cases, part of your stamina. Most attacks that require FP generally don't require very much and are much stronger than the average ability. If it ever falls below 0 however, you will die (after the battle ends if you are in one when it happens.) 30 FP a day and 5 FP a battle is deducted."
    return
    
label about_tod:
    scene bg mainmenu
    "As you do certain actions, time will pass. Keeping track of the Time of Day is extremely important. Some events can only happen at certain Time of Days. In addition, the time you go to sleep at influences how much SP you regain during the night."
    return
    
label about_sp:
    scene bg mainmenu
    "SP/Sleep Points serves as your fatigue and in some cases, part of your stamina. Most attacks that require SP generally don't require very much and are much stronger than the average ability. If it ever falls below 0 however, you will die (after the battle ends if you are in one when it happens.) 20 SP a day is deducted; sleeping reduces, reverses, or overcompensates for this. You gain 3 SP per hour slept."
    return
    
label about_char(some_char):
    scene bg fakefog
    $ in_debug = True
    if (some_char == "kazuki"):
        centered "%(kazukiGloss)s"
    if (some_char == "katherine"):
        centered "%(rinGloss)s"
    if (some_char == "jonathan"):
        centered "%(jonGloss)s"
    if (some_char == "wil"):
        centered "empty file"
    if (some_char == "proflaw"):
        centered "%(lawGloss)s"
    if (some_char == "masamune"):
        centered "%(masaGloss)s"
    if (some_char == "athena"):
        centered "%(athenaGloss)s"
    if (some_char == "natalie"):
        centered "%(natGloss)s"
    if (some_char == "tammy"):
        centered "%(tammyGloss)s"
    if (some_char == "lilian"):
        centered "%(liliGloss)s"
    if (some_char == "ultraman7"):
        centered "%(ult7Gloss1)s"
        centered "%(ult7Gloss2)s"
        centered "%(ult7Gloss3)s"
    $ in_debug = False
    return
