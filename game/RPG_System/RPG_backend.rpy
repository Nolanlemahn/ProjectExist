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
        
    def domchange(passedvar, passedvalue, bool_loud):
        renpy.call("domchange", passedvar, passedvalue, bool_loud)
        return
   
label domchange(passedvar, passedvalue, bool_loud):
    if passedvalue > 0:
        $ strchange = "+" + str(passedvalue) + " " +  passedvar
    else:
        $ strchange = str(passedvalue) + " " +  passedvar
    $ main_char.doChange(passedvar, passedvalue)
    if(bool_loud == 1):
        $ updateUIroutine = 2
    return
