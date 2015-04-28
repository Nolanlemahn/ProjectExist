init -2 python:
    scene_scope = {}

    def jump_break():
        renpy.end_replay()
        return
                
    def jump_in(label_string):
        scene_scope = {}
        scene_scope = base_scope.copy()
        if label_string not in special_cases:
            scene_scope.update(scopes[label_string])
        renpy.call_replay(label_string, scope=scene_scope)
        #renpy.quit(relaunch=True)
        return

    def store_reset():
        renpy.store.answers = []
    config.start_callbacks.append(store_reset)

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
        
        textbutton "(Test the Combat System)" xminimum 300 action Function(jump_in, "combat_test")
        textbutton "Welcome to San Francisco\nCommunity College" xminimum 300 action If(renpy.seen_label("Kazuki_1c"), Function(jump_in, "Kazuki_1b"))
        textbutton _("Return") action Return()