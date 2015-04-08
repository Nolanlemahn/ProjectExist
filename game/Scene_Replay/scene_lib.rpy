init python:
    def jump_break():
        if(hasattr(store, 'jumping_in')):
            if(store.jumping_in):
                renpy.end_replay()
        return
                
    def jump_in(label_string):
        store.jumping_in = True;
        scene_load(label_string)
        return
    
screen scene_replay:
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
        xminimum 300
        has vbox
        
        textbutton "Welcome to San Francisco\nCommunity College" xminimum 300 action If(renpy.seen_label("Kazuki_1c"), Function(jump_in, "Kazuki_1b"))
        textbutton _("Return") action Return()