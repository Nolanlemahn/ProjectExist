init -1 python:
    #Define the frame here!
    blank_frame_img = "menus/blank.png"
    sn_frame_img = "menus/FoxGameBox.png"
    sn_width = 400
    sn_height = 200
    top_pixels = 6
    snroutine = -1

init -1:
    #exactly where I want the sidenotes to be at/come in
    transform sn_at:
        xpos 1200 ypos 240
        linear 1.0 xpos 800
    #exactly where I want the sidenotes to leave
    transform sn_leave:
        xpos 800 ypos 240
        linear 1.0 xpos 1200

label sn_draw(select_tip):
    $ snroutine = 4
    $ selected_note = select_tip

    show screen side_note
    $ sn_resolver(select_tip)
    return

init -1 python:
    #remap for label
    def sn_draw(selected_sn):
        renpy.call("sn_draw", selected_sn)
        return
    # be responsible for showing image
    def sn_resolver(img):
        renpy.show(img, at_list = [sn_at])
        return

    def hide_side_note():
        if(store.in_side_note == True):
            store.snroutine = -1
            renpy.show(store.selected_note, at_list=[sn_leave])
        return
    
    def side_note_callback():
        if(hasattr(store, 'snroutine') and hasattr(store, 'selected_note')):
            if store.snroutine > 0:
                store.snroutine = store.snroutine - 1
                if store.snroutine == 1:
                    renpy.show(store.selected_note, at_list=[sn_leave])
                    renpy.hide_screen("side_note_tag")
                    store.snroutine = 0
            elif(store.snroutine == 0):
                renpy.show(store.selected_note, at_list=[sn_leave])
                renpy.hide(store.selected_note)
                store.snroutine = -1
        return
    config.interact_callbacks.append(side_note_callback)

    def show_sn(st, at, tt="something wrong"):
        tip = tt
        return Fixed(
            Frame(sn_frame_img, sn_width + 4, sn_height),
            VBox(
                Text("{size=[top_pixels]}\n{/size}%s" % tip, color="#fff", size=22, first_indent=6, rest_indent=6),
                xsize = sn_width - 2, ysize=sn_height
                ), 
            xminimum = sn_width, ysize=sn_height), None

screen side_note:
    tag side_note_tag
    vbox xalign 1.0 yalign 0.4 xsize 400 ysize 200:
        imagebutton:
            hover Frame(blank_frame_img, sn_width, sn_height)
            idle Frame(blank_frame_img, sn_width, sn_height)
            action (ToggleVariable("in_side_note", True, True), Hide("side_note"), hide_side_note())