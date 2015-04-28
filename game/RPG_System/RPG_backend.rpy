init python:    
    def updateUI(thischange):#UI for changes in stats
        ui.frame(xfill=False, xminimum=100, xmaximum=100, yminimum=(thischange * 30 + 10), ymaximum=50, xalign=0.5, yalign=0.0, style="game_box")
        ui.vbox(xalign=0.5)
        if(hasattr(store, 'updateUIroutine')):
            if store.updateUIroutine > 0:
                store.updateUIroutine = store.updateUIroutine - 1
                ui.text("%s" % (strchange))
            else:
                ui.text("")
        ui.close()
        return
        
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
