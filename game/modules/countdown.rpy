init -1 python:
    def img(name, color, x, y):#from 00themes
        rv = theme.OneOrTwoColor(name, color)
        if x is not None:
            rv = Frame(rv, x, y, tile=True)
        return rv

init -1:
    $ cdw_color = (255, 0, 0, 255)#red
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

init python:
    def menu_callback(mode, old_modes):
        if mode == "say" or mode == "nvl":
            renpy.hide_screen("countdown_tag")
            renpy.fix_rollback()
        if (renpy.in_fixed_rollback()):
            renpy.hide_screen("countdown_tag")
    config.mode_callbacks.append(menu_callback)
    
    def cd_set(start_time, end_time, target_str):
        #don't bother checking store
        store.time = start_time
        store.timer_range = end_time
        store.timer_jump = target_str
        return