screen say_prepend:
    if(not in_debug):
        if(showMCStatus):#the normal stats
            $ show_combatant_stats(main_char, .02, .01)
        if(clock):#maybe we don't even need to check this variable...?
            $ Calendar()
            $ Clocks()
        if(ui_check):
            $ updateUI(intchange)
        if(walletshow):
            $ Wallet()

##############################################################################
# Say
# TODO: CLEANUP
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:
    tag say
    use say_prepend
            
    ############################################
    # Defaults
    default side_image = None
    default two_window = False
    

    # The two window variant.
    vbox:
        style "say_two_window_vbox"
        if who:            
            window:
                style "say_who_window"
                text who:
                    id "who"
        window:
            id "window"
            has vbox:
                style "say_vbox"
            text what id "what"
        # If there's a side image, display it above the text.
        if side_image:
            add side_image
        else:
            add SideImage() xalign 0.0 yalign 1.0
      
    # Use the quick menu.
    use left_quick_menu
    use quick_menu
    if(battle_mode):
        $ renpy.block_rollback()

screen multiple_say:
    tag say
    $ thisBlock = multiple[0]
    $ totalBlocks = multiple[1]
    if(thisBlock == 0):
      use say_prepend
            
    ############################################
    # Defaults
    default side_image = None
    default two_window = False
    

    # The two window variant.
    vbox:
        xsize config.screen_width/totalBlocks
        xpos config.screen_width/totalBlocks*(thisBlock - 1)
        style "say_two_window_vbox"
        if who:            
            window:
                style "say_who_window"
                text who:
                    id "who"
        window:
            id "window"
            has vbox:
                style "say_vbox"
            text what id "what"
        # If there's a side image, display it above the text.
        if side_image:
            add side_image
        else:
            add SideImage() xalign 0.0 yalign 1.0
      
    # Use the quick menu.
    if(thisBlock == 0):
      use left_quick_menu
      use quick_menu
    if(battle_mode):
        $ renpy.block_rollback()

screen choice:
    $ in_menu = True
    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        vbox:
            style "menu"
            spacing 2
            for caption, action, chosen in items:
                if action:  
                    button:
                        action action
                        style "menu_choice_button"                        
                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"
    $ in_menu = False
        
init -2 python:
    config.narrator_menu = True
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu
        
##############################################################################
# Nvl
#
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl_hard:
    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"
screen nvl:
    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    use left_quick_menu
    use quick_menu
        
