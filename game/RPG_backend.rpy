#BaseDamage = (((((((Level × 2 ÷ 5) + 2) × BasePower × [Sp]Atk ÷ 50) ÷ [Sp]Def) × Mod1) + 2) × CH × Mod2 × R ÷ 100) × STAB × Type1 × Type2 × Mod3)
#^ rewrite that algorithm; we don't have [Sp]
#oh wait yes we do

init -1:
    $ attack_choice = "Nothing"
    $ eattack_choice = "Nothing"
    $ firstturn = 0
    
    $ stance = ""
    $ curr_turn = ""
    $ curr_eval = ""
    $ special_initiative = False
    $ able_to_flee = False
    $ first_turn = False
    $ some_move = ""
    
    $ batcheckpoint = 0
    
    # a big damn mess
    $ movecount = 0
    $ chosenmove = ""
    $ movenumbers = [0,0,0,0]
    $ movenames = ["","","","","","","",""]
    $ movecosts = ["","","","","","","","","","","","","","","",""]
    $ movename1 = ""
    $ movename2 = ""
    $ movename3 = ""
    $ movename4 = ""
    $ movename5 = ""
    $ movename6 = ""
    $ moveexists = 0
    
    $ power = 0
    $ accuracy = 0
    $ priority = 0
    $ parameter = ""
    $ parameterplus = 0
    $ typea = ""
    $ typeb = ""
    $ damage = 0
    
    $ m1damage = 0
    $ e1damage = 0
    $ m1move = ""
    $ e1move = ""
    
    $ m1accmod = 0
    $ m1evmod = 0
    $ m1power = 0
    $ m1accuracy = 0
    $ m1priority = 0
    $ m1parameter = ""
    $ m1parameterplus = 0
    $ m1mess1 = ""
    $ m1mess2 = ""
    $ m1status = ""
    $ m1cost = ["",""]
    
    $ e1accmod = 0
    $ e1evmod = 0
    $ e1power = 0
    $ e1accuracy = 0
    $ e1priority = 0
    $ e1parameter = ""
    $ e1parameterplus = 0
    $ e1mess1 = ""
    $ e1mess2 = ""
    $ e1status = ""
    $ e1cost = ["",""]
    
    $ m1pass = True
    $ e1pass = False
    

init python:
    def check_status(target):
        if ((target == "m1") and (hasattr(store, 'm1status'))):
            if (store.m1status == "stunned"):
                store.m1status = "none"
                return (True, " was stunned and failed to move!")
        if ((target == "e1") and (hasattr(store, 'e1status'))):
            if (store.e1status == "stunned"):
                store.e1status = "none"
                return (True, " was stunned and failed to move!")
        return
                
    def mini_combat_callback():
        if (hasattr(store, 'm1hp') and (single_combat_check == False)):
            if store.m1hp < 1:
                store.m1hp = 0
                renpy.jump("battle_death")
        if (hasattr(store, 'e1hp') and (single_combat_check == False)):
            if store.e1hp < 1:
                store.e1hp = 0
                renpy.jump("battle_end")
        return
    config.python_callbacks.append(mini_combat_callback)
    
    def updateUI(thischange):#UI for changes in stats
        ui.frame(xfill=False, xminimum=100, xmaximum=100, yminimum=(thischange * 30 + 10), ymaximum=50, xalign=0.5, yalign=0.0, style="game_box")
        ui.vbox(xalign=0.5)
        if (hasattr(store, 'updateUIroutine')):
            if store.updateUIroutine > 0:
                store.updateUIroutine = store.updateUIroutine - 1
                ui.text("%s" % (strchange))
            else:
                ui.text("")
        ui.close()
        return
    
    def mini_death_callback():#constantly check for instadeath
        if (hasattr(store, 'main_char_currentBelly') and (single_death_check == False)):
            if store.main_char_currentBelly < 1:
                store.main_char_currentBelly = 0
                renpy.jump("text_died_of_hunger")
        if (hasattr(store, 'main_char_currentSleep') and (single_death_check == False)):
            if store.main_char_currentSleep < 1:
                store.main_char_currentSleep = 0
                renpy.jump("text_died_of_sleep")
        return
    config.python_callbacks.append(mini_death_callback)

                
    def checkSizeTwo():
        if (persistent.useDyslexic == True):
            return 13
        else:
            return 24
    
    def show_stats(name, level, hp, maxhp, fp, maxfp, sp, maxsp, xp, maxxp, xal1, yal1):
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
        ui.text("XP", size=checkSizeTwo())
        ui.close()
        ui.vbox()
        ui.bar(maxhp, hp, xminimum=180, xmaximum=180)
        ui.bar(maxfp, fp, xminimum=180, xmaximum=180)
        ui.bar(maxsp, sp, xminimum=180, xmaximum=180)
        ui.bar(maxxp, xp, xminimum=180, xmaximum=180)
        ui.close()
        ui.vbox() # Level from (hp/maxhp)
        if (hp < 100):
            ui.text(" %d/%d" % (hp, maxhp), xalign=1.0, size=checkSizeTwo())
        else:
            ui.text("%d/%d" % (hp, maxhp), xalign=1.0, size=checkSizeTwo())
        if (fp < 100):
            ui.text(" %d/%d" % (fp, maxfp), xalign=1.0, size=checkSizeTwo())
        else:
            ui.text("%d/%d" % (fp, maxfp), xalign=1.0, size=checkSizeTwo())
        if (sp < 100):
            ui.text(" %d/%d" % (sp, maxsp), xalign=1.0, size=checkSizeTwo())
        else:
            ui.text("%d/%d" % (sp, maxsp), xalign=1.0, size=checkSizeTwo())
        if (xp < 100):
            ui.text("%d/%d" % (xp, maxxp), xalign=1.0, size=checkSizeTwo())
        elif (xp < 1000):
            ui.text("%d/%d" % (xp, maxxp), xalign=1.0, size=checkSizeTwo())
        else:
            ui.text("%d/%d" % (xp, maxxp), xalign=1.0, size=checkSizeTwo())
        ui.close()
        ui.close()
        return
        
    def show_stats_noXP(name, level, hp, maxhp, fp, maxfp, sp, maxsp, xp, maxxp, xal1, yal1):
        ui.frame(xfill=False, xminimum = 330, yminimum=None, xalign=(xal1), yalign=(yal1))
        ui.hbox()
        ui.text("%s" % name, size=checkSizeTwo())
        ui.text("  Lv. %d" % level, xalign=1.0, size=checkSizeTwo())
        ui.close()
        ui.frame(xfill=False, xminimum = 330, yminimum=None, xalign=(xal1), yalign=(yal1 + 0.05))
        ui.hbox()
        ui.vbox()
        ui.text("HP", size=checkSizeTwo())
        ui.text("FP", size=checkSizeTwo())
        ui.text("SP", size=checkSizeTwo())
        #ui.text("XP", size=checkSizeTwo())
        ui.close()
        ui.vbox()
        ui.bar(maxhp, hp, xminimum=180, xmaximum=180)
        ui.bar(maxfp, fp, xminimum=180, xmaximum=180)
        ui.bar(maxsp, sp, xminimum=180, xmaximum=180)
        ui.close()
        ui.vbox() # Level from (hp/maxhp)
        if (xal1 == 0.98):
            ui.text("?/?", xalign=1.0, size=checkSizeTwo())
            ui.text("?/?", xalign=1.0, size=checkSizeTwo())
            ui.text("?/?", xalign=1.0, size=checkSizeTwo())
        else:
            if (hp < 100):
                ui.text(" %d/%d" % (hp, maxhp), xalign=1.0, size=checkSizeTwo())
            else:
                ui.text("%d/%d" % (hp, maxhp), xalign=1.0, size=checkSizeTwo())
            if (fp < 100):
                ui.text(" %d/%d" % (fp, maxfp), xalign=1.0, size=checkSizeTwo())
            else:
                ui.text("%d/%d" % (fp, maxfp), xalign=1.0, size=checkSizeTwo())
            if (sp < 100):
                ui.text(" %d/%d" % (sp, maxsp), xalign=1.0, size=checkSizeTwo())
            else:
                ui.text("%d/%d" % (sp, maxsp), xalign=1.0, size=checkSizeTwo())
        ui.close()
        ui.close()
        return