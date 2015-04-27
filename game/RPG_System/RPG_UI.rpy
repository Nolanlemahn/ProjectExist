label inventory_crap:
    $ inventory_see = False
    $ notin_other_stats = False
    window show
    with dissolve
    nvln "Not working atm."
    window hide
    with dissolve
    nvl clear
    $ inventory_see = True
    $ notin_other_stats = True
    return
    
label battle_inventory:
    window show
    with dissolve
    nvln "Not working atm."
    window hide
    with dissolve
    nvl clear
    jump m1_1v1_turna
    
label other_stats:#show combat stats
    $ notin_other_stats = False
    window show
    with dissolve
    if(not ingame):
        nvln "Progress farther in the game to use this screen."
    else:
        nvln "(Expect this screen to be unavailable in non-dev/debug mode in the final release.)\nStrength: [main_char_stats[0]]\nDexterity: [main_char_stats[1]]\nSpeed: [main_char_stats[2]]\nResilience: [main_char_stats[3]]\nIntelligence: [main_char_stats[4]]\nSpirit: [main_char_stats[5]]\nAbility 1: [main_char_ABI_SLO1] || Level [main_char_ABI_SLOL1]\nAbility 2: [main_char_ABI_SLO2] || Level [main_char_ABI_SLOL2]"
    window hide
    with dissolve
    nvl clear
    $ notin_other_stats = True
    return
    
init python:
    def show_combatant_stats(combatant, xal1, yal1, showXP = True):
        name = combatant.name
        level = combatant.level
        hp = combatant.currentHP
        maxhp = combatant.maxHP
        fp = combatant.currentBelly
        maxfp = combatant.maxBelly
        sp = combatant.currentSleep
        maxsp = combatant.maxSleep
        xp = combatant.currentXP
        maxxp = combatant.maxXP
        ui.frame(xfill=False, xminimum = 330, yminimum=None, xalign=(xal1), yalign=(yal1), style="game_box")
        ui.hbox()
        ui.text("%s" % name, size=checkSizeTwo())
        ui.text("  Lv. %d" % level, xalign=1.0, size=checkSizeTwo())
        ui.close()
        ui.frame(xfill=False, xminimum = 330, yminimum=None, xalign=(xal1), yalign=(yal1 + 0.05), style="game_box")
        ui.hbox()
        ui.vbox()
        ui.text("HP", size=checkSizeTwo())
        ui.text("FP", size=checkSizeTwo())
        ui.text("SP", size=checkSizeTwo())
        if(showXP):
            ui.text("XP", size=checkSizeTwo())
        ui.close()
        ui.vbox()
        ui.bar(maxhp, hp, xminimum=180, xmaximum=180)
        ui.bar(maxfp, fp, xminimum=180, xmaximum=180)
        ui.bar(maxsp, sp, xminimum=180, xmaximum=180)
        if(showXP):
            ui.bar(maxxp, xp, xminimum=180, xmaximum=180)
        ui.close()
        ui.vbox() # Level from (hp/maxhp)
        if(hp < 100):
            ui.text(" %d/%d" % (hp, maxhp), xalign=1.0, size=checkSizeTwo())
        else:
            ui.text("%d/%d" % (hp, maxhp), xalign=1.0, size=checkSizeTwo())
        if(fp < 100):
            ui.text(" %d/%d" % (fp, maxfp), xalign=1.0, size=checkSizeTwo())
        else:
            ui.text("%d/%d" % (fp, maxfp), xalign=1.0, size=checkSizeTwo())
        if(sp < 100):
            ui.text(" %d/%d" % (sp, maxsp), xalign=1.0, size=checkSizeTwo())
        else:
            ui.text("%d/%d" % (sp, maxsp), xalign=1.0, size=checkSizeTwo())
        if(showXP):
            if(xp < 100):
                ui.text("%d/%d" % (xp, maxxp), xalign=1.0, size=checkSizeTwo())
            elif(xp < 1000):
                ui.text("%d/%d" % (xp, maxxp), xalign=1.0, size=checkSizeTwo())
            else:
                ui.text("%d/%d" % (xp, maxxp), xalign=1.0, size=checkSizeTwo())
        ui.close()
        ui.close()
        return