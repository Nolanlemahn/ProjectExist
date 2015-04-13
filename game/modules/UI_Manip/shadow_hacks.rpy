init python:
    #Comment this crap later
    def shadow_set(x, y, menu_str, target_str):
        #don't bother checking store
        store.mouse_hack_x = x
        store.mouse_hack_y = y
        store.hack_label = menu_str
        store.landing_label = target_str
        return
        
    def shadow_hack():
        old_pref = _preferences.mouse_move
        store.old_mouse = config.mouse
        
        _preferences.mouse_move = True
        config.mouse = { 'default' : [ ('menus/shadow_mouse.png', 0, 0)] }
        
        renpy.hide_screen("countdown_tag")
        renpy.set_mouse_pos(store.mouse_hack_x, store.mouse_hack_y, 0.5)
        _preferences.mouse_move = old_pref
        store.shadowtime = 0.7
        renpy.jump(store.hack_label)
        #renpy.pause(1.0)
        return

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