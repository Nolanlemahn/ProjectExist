label rollfind:
    if not(persistent.choice_rollback):
        $ renpy.block_rollback()
    return
    
label install_prologue:
    scene bg mainmenu
    $ in_debug = True
    #$ persistent.standalone_dlc_avail = True
    #$ persistent.dlc1_installed = True
    #"The DLC was installed."
    "This build of Project Exist does not support or include DLC#1."
    $ in_debug = False
    return
    
label rollback_mode:
    scene bg mainmenu
    $ in_debug = True
    if (not persistent.all_rollback):
        "Right now, rollback is disabled everywhere."
        menu:
            extend ""
            "Disable it only at choices":
                $ persistent.all_rollback = True
                $ persistent.choice_rollback = False
                "Done!"
            "Enable it everywhere":
                $ persistent.all_rollback = True
                $ persistent.choice_rollback = True
                "Done!"
            "Keep it that way":
                "Very well."
    elif (not persistent.choice_rollback):
        "Right now, rollback is only disabled at choices."
        menu:
            extend ""
            "Disable it everywhere":
                $ persistent.all_rollback = False
                $ persistent.choice_rollback = False
                "Done!"
            "Enable it everywhere":
                $ persistent.all_rollback = True
                $ persistent.choice_rollback = True
                "Done!"
            "Keep it that way":
                "Very well."
    else:
        "Right now, rollback is enabled everywhere."
        menu:
            extend ""
            "Disable it everywhere":
                $ persistent.all_rollback = False
                $ persistent.choice_rollback = False
                "Done!"
            "Disable it only at choices":
                $ persistent.all_rollback = True
                $ persistent.choice_rollback = False
                "Done!"
            "Keep it that way":
                "Very well."
    $ in_debug = False
    return
    
label unlock_code:
    scene bg mainmenu
    $ in_debug = True
    $ unlockdevice = renpy.input("Type in the unlock code.")
    if (unlockdevice=="debug"):
        $ persistent.debugmenu_seen = True
        $ persistent.debugmenu_installed = True
        "The Debug Menu was unlocked."
    elif (unlockdevice=="beta"):
        $ persistent.imabetatester = True
        $ persistent.imabetatester_seen = True
        "Any beta features have been unlocked."
    elif(unlockdevice=="dev"):
        $ config.locked = False
        $ config.developer = True
        $ config.locked = True
        "Set config.developer to True."
    else:
        "\"[unlockdevice]\" does not appear to be a valid unlock/cheat code. Ensure spelling, punctuation, and capitalization are all correct."
    $ in_debug = False
    return

label install(addon):
    scene bg mainmenu
    $ in_debug = True
    if (addon=="debug"):
        $ persistent.debugmenu_installed = True
        "The Debug Menu was enabled."
    if (addon=="rollback"):
        $ persistent.choice_rollback = True
        "Rollback beyond choices was enabled."
    if (addon=="beta"):
        $ persistent.imabetatester = True
        "Beta access was enabled."
    $ in_debug = False
    return
    

label uninstall(addon):
    scene bg mainmenu
    $ in_debug = True
    if (addon=="debug"):
        $ persistent.debugmenu_installed = False
        "The Debug Menu was disabled."
    if (addon=="rollback"):
        $ persistent.choice_rollback = False
        "Rollback beyond choices was disabled."
    if (addon=="beta"):
        $ persistent.imabetatester = False
        "Beta access was disabled."
    $ in_debug = False
    return
    
screen install_extras:
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5
        xmaximum 800
        ymaximum 500
        
        vbox:
            textbutton "Unlock/Cheat Code" xminimum 300 action ui.callsinnewcontext("unlock_code")
            if (persistent.debugmenu_seen):
                if (persistent.debugmenu_installed):
                    textbutton "Debug Menu [[X]" xminimum 300 action ui.callsinnewcontext("uninstall", "debug")
                else:
                    textbutton "Debug Menu [[O]" xminimum 300 action ui.callsinnewcontext("install", "debug")
            #if (persistent.cheat_disable_disable_rollback_seen):
            
            if (persistent.imabetatester_seen):
                if (persistent.imabetatester):
                    textbutton "Beta Access [[X]" xminimum 300 action ui.callsinnewcontext("uninstall", "beta")
                else:
                    textbutton "Beta Access [[O]" xminimum 300 action ui.callsinnewcontext("install", "beta")
                    
            if not (persistent.dlc1_installed):
                textbutton "Install DLC#1: Prologue" xminimum 300 action ui.callsinnewcontext("install_prologue")
            textbutton "Return" action ShowMenu("more_menu")
            bar adjustment adj style "vscrollbar"
