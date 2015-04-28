# sidenote defines
# each sn image needs a corresponding call in sn_draw
image sn demo = DynamicDisplayable(show_sn, tt=
    "This is a demo side note. You may click to dismiss, or you may progress to the next dialogue screen. It will dismiss itself after three "+
    "interactions.")
image sn gre = DynamicDisplayable(show_sn, tt=
    "GRE is short for Graduate Record Examination, a standardized test developed by " + 
    "the Educational Testing Service (ETS) in the United States in order to measure and compare graduate school candidates.")
image sn siebener = DynamicDisplayable(show_sn, tt=
    "A Siebener refers to a 7 series BMW, just as a bimmer refers to any BMW car. A beemer actually refers to a motorcycle made by BMW.")
image sn frank = DynamicDisplayable(show_sn, tt=
    "Frank Anthoni Bruni was the chief restaurant critic of the New York Times from 2004 to 2009.")
image sn jaane = DynamicDisplayable(show_sn, tt=
    "\"Jaa ne\" {font=fonts/gulim.ttf}(じゃあね){/font} translates to \"see ya\". At least roughly.")


label sn_draw(select_tip):
    $ selected_note = select_tip
    $ snroutine = 3
    show screen side_note
    if(select_tip=="sn demo"):
        show sn demo:
            xpos 1200 ypos 240
            linear 1.0 xpos 800
            
    if(select_tip=="sn gre"):
        show sn gre:
            xpos 1200 ypos 240
            linear 1.0 xpos 800
            
    if(select_tip=="sn siebener"):
        show sn siebener:
            xpos 1200 ypos 240
            linear 1.0 xpos 800
            
    if(select_tip=="sn frank"):
        show sn frank:
            xpos 1200 ypos 240
            linear 1.0 xpos 800

    if(select_tip=="sn jaane"):
        show sn jaane:
            xpos 1200 ypos 240
            linear 1.0 xpos 800
    return

init python:
    def sn_draw(selected_sn):
        renpy.call("sn_draw", selected_sn)
        return
