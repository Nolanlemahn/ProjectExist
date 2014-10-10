#sidenote clock wallet calendar systems
init -1:
    transform tip_right:
        xpos 800 ypos 240
        linear 1.0 xpos 1200

init python:
    #import locale
    #locale.setlocale(locale.LC_ALL, 'en_US')
    style.sn_button = Style(style.button)
    style.sn_button.background = Frame("menus/emptyframe.png", 400,200)
    style.sn_button.hover_background = "#FFFFFF"
    style.sn_button.selected_background = Frame("menus/emptyframe.png", 400,200)
    style.sn_button_text = Style(style.button_text)
    style.sn_button_text.color = "#FFFFFF"
    style.sn_button_text.hover_color = "#FFFFFF"
    style.sn_button_text.selected_color = "#FFFFFF"
    style.sn_button_text.xalign = 0.0
    style.sn_button_text.yalign = 0.03
    
    def hide_side_note():
        if (store.in_side_note == True):
            store.snroutine = -1
            renpy.show(store.selected_note, at_list=[tip_right])
        return
    
    def side_note_callback():
        if (hasattr(store, 'snroutine') and hasattr(store, 'selected_note')):
            if store.snroutine > 0:
                store.snroutine = store.snroutine - 1
                if store.snroutine == 1:
                    renpy.show(store.selected_note, at_list=[tip_right])
                    renpy.hide_screen("side_note_tag")
                    store.snroutine = 0
            elif(store.snroutine == 0):
                renpy.show(store.selected_note, at_list=[tip_right])
                renpy.hide(store.selected_note)
                store.snroutine = -1
        return
    config.interact_callbacks.append(side_note_callback)

    def show_sn(st, at, tt="something wrong"):
        tip = tt
        return Fixed(
            Image("menus/buttonframe.png"),
            VBox("menus/topline.png",
                Text("%s" % tip, color="#fff", size=22, xmaximum=400, first_indent=6, rest_indent=6))), None

            
    #def Alert():
    #    if(dev_alert == None):
    #        ui.frame(xfill=False, xminimum = 33, yminimum=None, xalign=0.801, yalign = 0.76, style='clipFrame')
    #        ui.vbox()
    #        ui.text("", xalign=1.0, size=checkSizeTwo())
    #        ui.close()
    #    elif(dev_alert == "hide"):
    #        return
    #    else:
    #        ui.textbutton("!", style=style.dev_button, text_style = style.dev_button_text, xalign=0.801, yalign = 0.760, clicked = ui.callsinnewcontext("small_dir", dev_alert), xminimum=22, yminimum=37)

    
    def answer_add(new_answer):
        answers.append(new_answer)
        return
    
    def python_pass():
        return

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init -1:
    $ cdw_color = (255, 0, 0, 255)#red
    $ style.create("game_box", "frame")
    $ style.game_box.background = Frame("menus/FoxGameBox.png", 25, 25)
    $ style.create("cd_barw", "bar")
    $ style.cd_barw.left_bar = img("menus/thslider_full.png", cdw_color, 12, 0)
    $ style.cd_barw.right_bar = img("menus/thslider_empty.png", cdw_color, 12, 0)
    $ style.cd_barw.thumb = img("menus/thslider_thumb.png", cdw_color, None, None)
    $ style.cd_barw.hover_left_bar = img("menus/thslider_full.png", cdw_color, 12, 0)
    $ style.cd_barw.hover_right_bar = img("menus/thslider_empty.png", cdw_color, 12, 0)
    $ style.cd_barw.hover_thumb = img("menus/thslider_thumb.png", cdw_color, None, None)
    
    $ cd_color = (255, 255, 255, 255)#white
    $ style.create("cd_bar", "bar")
    $ style.cd_bar.left_bar = img("menus/thslider_full.png", cd_color, 12, 0)
    $ style.cd_bar.right_bar = img("menus/thslider_empty.png", cd_color, 12, 0)
    $ style.cd_bar.thumb = img("menus/thslider_thumb.png", cd_color, None, None)
    $ style.cd_bar.hover_left_bar = img("menus/thslider_full.png", cd_color, 12, 0)
    $ style.cd_bar.hover_right_bar = img("menus/thslider_empty.png", cd_color, 12, 0)
    $ style.cd_bar.hover_thumb = img("menus/thslider_thumb.png", cd_color, None, None)

screen countdown:
    tag countdown_tag
    if(not renpy.in_fixed_rollback()):
        key "rollback" action [[]]
        timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.1), false=[Hide('countdown'), Jump(timer_jump)])
        if time > 3:
            bar value time range timer_range xalign 0.5 yalign 0.33 xsize 300 style "cd_bar"
            text str("%.1f" % time) xalign .5 ypos .25 color "#FFFFFF" size 72
        elif time > 0:
            bar value time range timer_range xalign 0.5 yalign 0.33 xsize 300 style "cd_barw"
            text str("%.1f" % time) xalign .5 ypos .25 color "#F00000" size 72

screen side_note:
    tag side_note_tag
    vbox xalign 1.0 yalign 0.4 xsize 400 ysize 200:
        imagebutton:
            hover "menus/emptyframe.png"
            idle "menus/emptyframe.png"
            #Thorium look over here
            action (ToggleVariable("in_side_note", True, True), Hide("side_note"), hide_side_note())

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

label triple_min(interval):
    $ minutes = minutes + interval
    "... "
    $ minutes = minutes + interval
    extend "... "
    $ minutes = minutes + interval
    extend "..."
    return

screen button:
    if (dev_screen == "pass"):
        $ python_pass()
    elif ((dev_screen == "dream") and persistent.dev_commentary):
        vbox xalign 1.0 yalign 0.717:
            textbutton "(Reference)" action Help("game/dev/sleepamnesia.pdf") style "dev_button" text_style "dev_button_text"
    elif persistent.dev_commentary:
        vbox xalign 1.0 yalign 0.717:
            textbutton "(No Reference)" style "dev_button" text_style "dev_button_text"

label pre_update:
    $ in_debug = True
    scene bg mainmenu
    $ updater.update("http://projectexist.net/pe_updates/updates.json", restart=True)
    $ in_debug = False
    return
    
label dyslexic:
    scene bg blackdrop
    "{font=OpenDyslexic-Regular.otf}{size=20}When the game is set to dyslexic-mode, it uses this font. It is known as OpenDyslexic, which is 
     available at {a=http://dyslexicfonts.com}http://dyslexicfonts.com{/a}. This is a beta feature.{/size}{/font}"
    "{font=calibri.ttf}{size=26}For comparison, this is the normal font. Changing the font unlocks absolutely nothing.{/size}{/font}"
    menu:
        extend ""
        "{font=OpenDyslexic-Regular.otf}Change to OpenDyslexic!{/font}":
            $ persistent.useDyslexic = True
            "The default font is now OpenDyslexic. The game will now reload."
            $ renpy.reload_script()
        "Change to calibri":
            $ persistent.useDyslexic = False
            "The default font is now calibri. The game will now reload."
            $ renpy.reload_script()
        "Change nothing":
            "Nothing was changed."
    return

# this game purposefully uses multiple questions to get an answer from the player in order to get an answer. generally speaking, this fakes the feel of an actual conversation
# (after all, most decisions and or conclusions are the result of a discussion rather than a quick and easy computer prompt.
# thus, even though there may be two questions as part of a decision with 2 answers each, there may be three possible registratable answers for a single question rather than a two for two

init python:    
    #!URGENT : THIS CODE REALLY NEEDS A REWRITE!#
    def time_callback():#constantly calculate the time
        if (hasattr(store, 'minutes')):
            if (store.minutes > 1440):
                store.minutes = store.minutes - 1440
                store.theweekday = store.theweekday + 1
                store.theday = store.theday + 1
                store.dayofyear = dayofyear + 1
                
        if (hasattr(store, 'theweekday')):#setweekday
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
                
        if (hasattr(store, 'theday')):#monthlim
            if store.theday > store.daylim:
                store.theday = store.theday - store.daylim
                
        if (hasattr(store, 'themonth')):#setmonth
            if store.themonth == 1:
                store.stringmonth = "January"
                store.daylim = 31
            if store.themonth == 2:
                store.stringmonth = "February"
                if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
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
            
            if (hasattr(store, 'dayofyear') and hasattr(store, 'yearlim')):#yearstuff
               if store.dayofyear > store.yearlim:
                   store.dayofyear = store.dayofyear - store.yearlim
                   store.theyear = store.theyear + 1
               if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
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
        if (minutes > 719):
            if ((minutes - (int(minutes/60))*60) < 10):
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
            if ((minutes - (int(minutes/60))*60) < 10):
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