#clock wallet calendar systems
init -1:        
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0

label com_slide(message):
    if passedvalue > 0:
        $ strchange = "+" + str(passedvalue) + " " +  passedvar
    else:
        $ strchange = str(passedvalue) + " " +  passedvar
    if(passedvar == "HP"):
        if(not fight_is_1v1):
            $ main_char_currentHP = main_char_currentHP + passedvalue
    elif(passedvar == "FP"):
        if(not fight_is_1v1):
            $ main_char_currentBelly = main_char_currentBelly + passedvalue
    elif(passedvar == "SP"):
        if(not fight_is_1v1):
            $ main_char_currentSleep = main_char_currentSleep + passedvalue
    if(bool_loud == 1):
        $ thisroutine = 2
    return

label audio_memory:
    return

label pre_update:
    $ in_debug = True
    scene bg mainmenu
    $ updater.update("http://projectexist.net/pe_updates/updates.json", restart=True)
    $ in_debug = False
    return


# this game purposefully uses multiple questions to get an answer from the player in order to get an answer. generally speaking, this fakes the feel of an actual conversation
# (after all, most decisions and or conclusions are the result of a discussion rather than a quick and easy computer prompt.
# thus, even though there may be two questions as part of a decision with 2 answers each, there may be three possible registratable answers for a single question rather than a two for two

init python:
    def com_slide(message):
        renpy.call("com_slide", message)
        return

    def time_callback():#constantly calculate the time
        if(hasattr(store, 'minutes')):
            if(store.minutes > 1440):
                store.minutes = store.minutes - 1440
                store.theweekday = store.theweekday + 1
                store.theday = store.theday + 1
                store.dayofyear = dayofyear + 1
                
        if(hasattr(store, 'theweekday')):#setweekday
            if store.theweekday > 7:
                store.theweekday = store.theweekday - 7
            if store.theweekday == 1:
                store.stringweekday = "Sunday"
            elif store.theweekday == 2:
                store.stringweekday = "Monday"
            elif store.theweekday == 3:
                store.stringweekday = "Tuesday"
            elif store.theweekday == 4:
                store.stringweekday = "Wednesday"
            elif store.theweekday == 5:
                store.stringweekday = "Thursday"
            elif store.theweekday == 6:
                store.stringweekday = "Friday"
            elif store.theweekday == 7:
                store.stringweekday = "Saturday"
            else:
                store.stringweekday = "Error"
                
        if(hasattr(store, 'theday')):#monthlim
            if store.theday > store.daylim:
                store.theday = store.theday - store.daylim
                
        if(hasattr(store, 'themonth')):#setmonth
            if store.themonth == 1:
                store.stringmonth = "January"
                store.daylim = 31
            if store.themonth == 2:
                store.stringmonth = "February"
                if((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                    store.daylim = 29
                else:
                    store.daylim = 28
            if store.themonth == 3:
                store.stringmonth = "March"
                store.daylim = 31
            if store.themonth == 4:
                store.stringmonth = "April"
                store.daylim = 30
            if store.themonth == 5:
                store.stringmonth = "May"
                store.daylim = 31
            if store.themonth == 6:
                store.stringmonth = "June"
                store.daylim = 30
            if store.themonth == 7:
                store.stringmonth = "July"
                store.daylim = 31
            if store.themonth == 8:
                store.stringmonth = "August"
                store.daylim = 31
            if store.themonth == 9:
               store.stringmonth = "September"
               store.daylim = 30
            if store.themonth == 10:
               store.stringmonth = "October"
               store.daylim = 31
            if store.themonth == 11:
               store.stringmonth = "November"
               store.daylim = 30
            if store.themonth == 12:
               store.stringmonth = "December"
               store.daylim = 31
            
            if(hasattr(store, 'dayofyear') and hasattr(store, 'yearlim')):#yearstuff
               if store.dayofyear > store.yearlim:
                   store.dayofyear = store.dayofyear - store.yearlim
                   store.theyear = store.theyear + 1
               if((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                   store.yearlim = 366
               else:
                   store.yearlim = 365
        return
    config.python_callbacks.append(time_callback)
    
    style.clockFrame = Style(style.frame)
    style.clockFrame.background = Frame("menus/FoxClockClip.png", 25, 25)
    
    def Calendar():
        ui.frame(xfill=False, xminimum = 400, yminimum=None, xalign=1.0, yalign = 0.805, style='clockFrame')
        ui.vbox()
        ui.text("(%s) - %s %d %d" % (stringweekday, stringmonth, theday, theyear), xalign=1.0, size=checkSizeTwo())
        ui.close()
        return
        
    def Clocks():
        ui.frame(xfill=False, xminimum = 110, yminimum=None, xalign=1.0, yalign = 0.76, style='clockFrame')
        ui.vbox()
        if(minutes > 719):
            if((minutes - (int(minutes/60))*60) < 10):
                if((int(minutes/60)) == 12):
                    ui.text("12:0%d PM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=checkSizeTwo())
                else:
                    ui.text("%d:0%d PM" % ((int(minutes/60)-12), (minutes - (int(minutes/60))*60)), xalign=1.0, size=checkSizeTwo())
            else:
                if((int(minutes/60)) == 12):
                    ui.text("12:%d PM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=checkSizeTwo())
                else:
                    ui.text("%d:%d PM" % ((int(minutes/60)-12), (minutes - (int(minutes/60))*60)), xalign=1.0, size=checkSizeTwo())
        else:
            if((minutes - (int(minutes/60))*60) < 10):
                if((int(minutes/60)) == 0):
                    ui.text("12:0%d AM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=checkSizeTwo())
                else:
                    ui.text("%d:0%d AM" % ((int(minutes/60)), (minutes - (int(minutes/60))*60)), xalign=1.0, size=checkSizeTwo())
            else:
                if((int(minutes/60)) == 0):
                    ui.text("12:%d AM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=checkSizeTwo())
                else:
                    ui.text("%d:%d AM" % ((int(minutes/60)), (minutes - (int(minutes/60))*60)), xalign=1.0, size=checkSizeTwo())
        ui.close()
        return

    
    def Wallet():
        ui.frame(xfill=False, xminimum = 125, yminimum=None, xalign=0.899, yalign = 0.76, style='clipFrame')
        ui.vbox()
        ui.text("$%.2f" % main_char_cash, xalign=1.0, size=checkSizeTwo())
        ui.close()
        return