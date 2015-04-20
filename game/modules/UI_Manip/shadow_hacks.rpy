#######
# File name: shadow_hacks.rpy
# 
# Description: Move the mouse to a different menu choice.
# 
# Original author: Nolan/NintendoToad
# 
# Type: Library, Screen
# 
# Usage:
#     $ shadow_set(Integer, Integer, String, String)
#     $ shadow_hack()
#######

init python:
    #####
    # Function name: shadow_set()
    # 
    # Description: Prepare to move the mouse.
    # 
    # Parameters:
    # x - x coordinate to move to
    # y - y coordinate to move to
    # menu_str - the label that we jump to, it should be a nearly perfect
    # copy of the old menu.
    # target_str - the label that we jump to after menu_str
    # 
    # Returns: None
    #####
    def shadow_set(x, y, menu_str, target_str):
        #don't bother checking store
        store.mouse_hack_x = x
        store.mouse_hack_y = y
        store.hack_label = menu_str
        store.landing_label = target_str
        return

    #####
    # Function shadow_hack()
    # 
    # Description: Actually move the mouse.
    #
    # Returns: None
    #####
    def shadow_hack():
        old_pref = _preferences.mouse_move
        store.old_mouse = config.mouse
        
        #It seems that the default mouse is None. Consider getting standard
        #cursor.
        _preferences.mouse_move = True
        # Mouse is the same except change the cursor.
        config.mouse = { 'default' : [ ('menus/shadow_mouse.png', 0, 0)] }
        # Stop counting down
        renpy.hide_screen("countdown_tag")
        renpy.set_mouse_pos(store.mouse_hack_x, store.mouse_hack_y, 0.5)
        _preferences.mouse_move = old_pref
        store.shadowtime = 0.7
        renpy.jump(store.hack_label)
        #renpy.pause(1.0)
        return

label reset_shadow:
    $ config.mouse = old_mouse
    $ renpy.jump(landing_label)
    
screen shadow_down:
    key "game_menu" action [[]]
    key "hide_windows" action [[]]
    tag shadow_tag
        # move timer every 0.1 seconds
    timer 0.1 repeat True action If(shadowtime > 0,
        true=SetVariable('shadowtime', shadowtime - 0.1),
        false=[SetVariable('in_shadow_down', False),
            Hide('shadow_down'),
            Jump("reset_shadow")])

    if time < 0:
        # redundantly set in_countdown to False just in case
        $ in_shadow_down = False

label menu_template:
    show screen shadow_down
    # The menu would hold all of the choices from the previous menu
    menu:
        nmc ""
        "Today's lecture":
            jump fake_1
        "The upcoming test":
            jump fake_1
        "Nothing at all":
            jump fake_1
        "...":
            jump fake_1
    return
