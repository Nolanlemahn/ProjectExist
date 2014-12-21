init -1 python:
    #Define the frame here!
    blank_frame_img = "menus/blank.png"
    sn_frame_img = "menus/FoxGameBox.png"
    sn_width = 400
    sn_height = 200
    top_pixels = 6

init -1:
    transform tip_right:
        xpos 800 ypos 240
        linear 1.0 xpos 1200

init -1 python:
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
            Frame(sn_frame_img, sn_width, sn_height),
            VBox(
                Text("{size=[top_pixels]}\n{/size}%s" % tip, color="#fff", size=22, xmaximum=sn_width, first_indent=6, rest_indent=6)), ysize=sn_height), None

screen side_note:
    tag side_note_tag
    vbox xalign 1.0 yalign 0.4 xsize 400 ysize 200:
        imagebutton:
            hover Frame(blank_frame_img, sn_width, sn_height)
            idle Frame(blank_frame_img, sn_width, sn_height)
            action (ToggleVariable("in_side_note", True, True), Hide("side_note"), hide_side_note())