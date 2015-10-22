init -2:
    $ config.keymap.update({"input_up":[ 'K_UP', 'repeat_K_UP' ]})
    $ config.keymap.update({"input_down":[ 'K_DOWN', 'repeat_K_DOWN' ]})

init python:
    def modright(obj):
        step = obj.xadjustment.get_step()
        oldval = obj.xadjustment.get_value()
        obj.xadjustment.change(oldval + step)
    def modleft(obj):
        step = obj.xadjustment.get_step()
        oldval = obj.xadjustment.get_value()
        obj.xadjustment.change(oldval - step)
    def modup(obj):
        step = obj.yadjustment.get_step()
        oldval = obj.yadjustment.get_value()
        obj.yadjustment.change(oldval - step)
    def moddown(obj):
        step = obj.yadjustment.get_step()
        oldval = obj.yadjustment.get_value()
        obj.yadjustment.change(oldval + step)

#expects name of viewport object
screen vpkm(obj):
    $ local = renpy.get_widget(None, obj)
    key "input_right" action [[Function(modright, local)]]
    key "input_left" action [[Function(modleft, local)]]
    key "input_up" action [[Function(modup, local)]]
    key "input_down" action [[Function(moddown, local)]]
