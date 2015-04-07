#######
# File name: countdown.rpy
# 
# Description: Implements a countdown timer that changes colors and forces a 
# jump once the timer runs out.
# 
# Original author: Nolan/NintendoToad
# 
# Type: Library, Screen
# 
# Usage:
#     $ cd_set(Int, Int, String)
#     show screen countdown
#######

init -1 python:
    #####
    # Function name: img()
    # 
    # Descripiton: Transforms an image to be used with a Theme.
    # 
    # Parameters:
    # name - image to modify
    # color - a tuple of four integers (rgba)
    # x - the xborder
    # y - the y vorder
    # 
    # Returns: the transformed image
    #####
    def img(name, color, x, y):#from 00themes
        rv = theme.OneOrTwoColor(name, color)
        if x is not None:
            rv = Frame(rv, x, y, tile=True)
        return rv

init -4:
        # Other screens should behave differently or not appear if we are in
        # countdown.
    $ in_countdown = False

# declare styles for red/white countdown bar
init -1:
    $ cdw_color = (255, 0, 0, 255) # the color red
        # style for a red countdown bar
    $ style.create("cd_barw", "bar")
    $ style.cd_barw.left_bar = img("menus/thslider_full.png", cdw_color, 12, 0)
    $ style.cd_barw.right_bar = img("menus/thslider_empty.png", cdw_color, 12, 0)
    $ style.cd_barw.thumb = img("menus/thslider_thumb.png", cdw_color, None, None)
    $ style.cd_barw.hover_left_bar = img("menus/thslider_full.png", cdw_color, 12, 0)
    $ style.cd_barw.hover_right_bar = img("menus/thslider_empty.png", cdw_color, 12, 0)
    $ style.cd_barw.hover_thumb = img("menus/thslider_thumb.png", cdw_color, None, None)
    
    $ cd_color = (255, 255, 255, 255) # the color white
        # color for a white countdown bar.
    $ style.create("cd_bar", "bar")
    $ style.cd_bar.left_bar = img("menus/thslider_full.png", cd_color, 12, 0)
    $ style.cd_bar.right_bar = img("menus/thslider_empty.png", cd_color, 12, 0)
    $ style.cd_bar.thumb = img("menus/thslider_thumb.png", cd_color, None, None)
    $ style.cd_bar.hover_left_bar = img("menus/thslider_full.png", cd_color, 12, 0)
    $ style.cd_bar.hover_right_bar = img("menus/thslider_empty.png", cd_color, 12, 0)
    $ style.cd_bar.hover_thumb = img("menus/thslider_thumb.png", cd_color, None, None)
  
# Shows the bar as it depletes, and the timer. Recolors if necessary. Forces a 
# jump if necessary.
screen countdown:
    key "game_menu" action [[]]
    key "hide_windows" action [[]]
    tag countdown_tag
        # move timer every 0.1 seconds
    timer 0.1 repeat True action If(time > 0,
        true=SetVariable('time', time - 0.1),
        false=[SetVariable('in_countdown', False),
            Hide('countdown'),
            Jump(timer_jump)])
    if time > 3:
        # white bar for lots of time left
        bar value time range timer_range xalign 0.5 yalign 0.33 xsize 300 style "cd_bar"
        text str("%.1f" % time) xalign .5 ypos .25 color "#FFFFFF" size 72
    elif time > 0:
        # red bar otherwise
        bar value time range timer_range xalign 0.5 yalign 0.33 xsize 300 style "cd_barw"
        text str("%.1f" % time) xalign .5 ypos .25 color "#F00000" size 72
    if time < 0:
        # redundantly set in_countdown to False just in case
        $ in_countdown = False

init python:
    # Stop showing the countdown once the player makes a choice or runs out of
    # time.
    def menu_callback(mode, old_modes):
        if mode == "say" or mode == "nvl":
            renpy.hide_screen("countdown_tag")
            renpy.fix_rollback()
            store.in_countdown = False
        if (renpy.in_fixed_rollback()):
            renpy.hide_screen("countdown_tag")
            store.in_countdown = False
    config.mode_callbacks.append(menu_callback)
    

    #####
    # Function name: cd_set()
    # 
    # Descripiton: Sets countdown variables so that the screen functions
    # correctly.
    # 
    # Parameters:
    # start_time - time started with/number to start depleting from
    # end_time - time at which a jump is forced
    # target_str - where we force a jump to
    # 
    # Returns: None
    #####
    def cd_set(start_time, end_time, target_str):
        #don't bother checking store
        store.time = start_time
        store.timer_range = end_time
        store.timer_jump = target_str
        store.in_countdown = True
        return

label return_stub:
    return
