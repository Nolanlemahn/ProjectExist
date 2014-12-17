#this file controls the dyslexic addons
#usage:
#  style.default.font = checkDefaultFont()
#  textbutton "Dyslexic?" action ui.callsinnewcontext("dyslexic") text_style "dys_button_text"

init -1 python:#magic numbers
    dyslexic_size = 16
    normal_size = 26
    
image bg blackdrop = "#000000"

init -1 python hide:    
    if persistent.useDyslexic is None:
        persistent.useDyslexic = False
    if persistent.amDev is None:
        persistent.amDev = False

init -1 python:
    #these are additional functions meant for, to some extent, allowing font
    #files and sizes to be directly selected by screens if need be. In other words, 
    #we are hiding some of our hidden magic numbers here. (largely with recards 
    #to the dyslexic options)
    style.dys_button = Style(style.button_text)
    style.dys_button_text.font = "fonts/OpenDyslexic-Regular.otf"
    
    def checkDefaultFont():
        if (persistent.useDyslexic == True):
            return "fonts/OpenDyslexic-Regular.otf"
        else:
            return "fonts/calibri.ttf"

    def checkUserDev():
        if (persistent.amDev == True):
            return True
        else:
            return False

    def checkDefaultSize():
        if (persistent.useDyslexic == True):
            return dyslexic_size
        else:
            return normal_size
            
label dyslexic:
    scene bg blackdrop
    "{font=fonts/OpenDyslexic-Regular.otf}{size=20}When the game is set to dyslexic-mode, it uses this font. It is known as OpenDyslexic, which is 
     available at {a=http://dyslexicfonts.com}http://dyslexicfonts.com{/a}. This is a beta feature.{/size}{/font}"
    "{font=fonts/calibri.ttf}{size=26}For comparison, this is the normal font. Changing the font unlocks absolutely nothing.{/size}{/font}"
    menu:
        extend ""
        "{font=fonts/OpenDyslexic-Regular.otf}Change to OpenDyslexic!{/font}":
            $ persistent.useDyslexic = True
            "The default font is now OpenDyslexic. The game will now reload."
            $ renpy.reload_script()
        "Change to calibri":
            $ persistent.useDyslexic = False
            "The default font is now calibri. The game will now reload."
            $ renpy.reload_script()
        "Change nothing":
            "Nothing was changed."
    return