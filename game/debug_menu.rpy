init:
    image bg fake_game_menu = "drops/fakegamemenu.png"
    $ temp_minutes = 0
    $ old_clock = False
    
init python:
    def stringStack(list_strings):
        returnable = ""
        for s in list_strings:
            returnable = returnable + "\n" + s
        return returnable[1:]
    
    def ReturnStatusVariable(dev_putstat):
        if hasattr(store, dev_putstat):
            renpy.store.dev_inputhold = eval(dev_putstat)
            return True
        else:
            return False
            
    def ChangeVar(cv_a, cv_b):
        setattr(store, cv_a, cv_b)#:D
        return

label varmani:
    $ in_debug = True
    scene bg mainmenu
    $ dev_inputchecked = None
    $ dev_inputhold = None
    $ dev_worked = None
    $ dev_inputvara = renpy.input("Type in the variable you'd like to change. PLEASE don't try this for arrays. That's just not a good idea.")
    $ dev_inputvarb = None
    $ dev_inputchecked = ReturnStatusVariable(dev_inputvara)
    if dev_inputchecked:
        "That was a good variable! ^_^ [dev_inputvara] has a value of [dev_inputhold]."
        $ dev_inputvarb = renpy.input("What would you like to change it to?")
        $ dev_worked = ChangeVar(dev_inputvara, dev_inputvarb)
        "[dev_inputvara] has been changed!"
    else:
        "That variable doesn't exist. T_T."
    $ in_debug = False
    return

label stalkme:
    scene bg mainmenu
    $ in_debug = True
    scene bg mainmenu
    #$ renpy.watch("renpy.get_filename_line()", style = style.alertnow_text, xpos=1.0, xanchor='right', ypos=0.0, yanchor='top')
    #"I am now watching you. The line and filename you are in will be displayed in the upper-left corner. Please add this information to any reports pertaining to spelling/grammar errors. You will need to re-visit this menu item every time you launch the game - sorry!"
    "This is not necessary and is turned on by default."
    $ in_debug = False
    return

label basevars:
    $ in_debug = True
    scene bg mainmenu
    if(not ingame):
        "You need to progress farther in the game in order to use this."
    else:
        if(ingame == "Kazuki"):
            "Points with Lawrence: [points[0]]"
            extend "\nPoints with Natalie: [points[1]]"
            extend "\nPoints with Tamara: [points[2]]"
            extend "\nPoints with Lily: [points[3]]"
    $ in_debug = False
    return
    
label given_answers:
    scene bg mainmenu
    $ in_debug = True
    if(not ingame):
        "You need to progress farther in the game in order to use this."
    else:
        "You've given the following answers:\n"
        $ big_answer = stringStack(answers)        
        "[big_answer]"
    $ in_debug = False
    return

label toggle_dev(toggled_mode):
    scene bg mainmenu
    $ in_debug = True
    if(toggled_mode == "dev"):
        $ persistent.amDev = False
        "Developer Mode has been turned off. The game will now reload."
        $ renpy.reload_script()
    else:
        $ persistent.amDev = True
        "Developer Mode has been turned on. The game will now reload."
        $ renpy.reload_script()
    $ in_debug = False
    return
    
screen debug_menu:
    #start pure style/aesthetics values
    tag menu

    window:
        style "gm_root"
        
    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5
        xmaximum 800
        ymaximum 500
    
        vbox:
            textbutton _("Text History") action ShowMenu("text_history")
            textbutton "Change a variable" xminimum 300 action ui.callsinnewcontext("varmani")
            textbutton "View most common variables" xminimum 300 action ui.callsinnewcontext("basevars")
            textbutton "View given answers" xminimum 300 action ui.callsinnewcontext("given_answers")
            if(persistent.amDev):
                textbutton "Developer Mode [[O]" xminimum 300 action ui.callsinnewcontext("toggle_dev", "dev")
            else:
                textbutton "Developer Mode [[X]" xminimum 300 action ui.callsinnewcontext("toggle_dev", "non_dev")
            #textbutton "Skip to Choice" minimum 300 action Skip(True, False)
            textbutton "Current location in script" xminimum 300 action ui.callsinnewcontext("stalkme")
            textbutton "Return" action Return()
            bar adjustment adj style "vscrollbar"
