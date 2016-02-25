#######
# File name: dyslexic_support.rpy
# 
# Description: Implements a font swapper.
# 
# Original author: Nolan/NintendoToad
# 
# Type: Library, Screen
# 
# Usage:
#     style.default.font = checkDefaultFont()
#     textbutton "Dyslexic?" action ui.callsinnewcontext("dyslexic") text_style "dys_button_text"
#######

image bg blackdrop = "#000000"#black backgound redef just in case

#magic numbers
init -4 python:
    dyslexic_size = 16
    normal_size = 26


init -1 python hide:
    # persistent table  
    if persistent.useDyslexic is None:
        persistent.useDyslexic = False
    if persistent.amDev is None:
        persistent.amDev = False

init -3 python:
    # magic values and styles

        # style for buttons that are always Dyslexic-formatted
    style.dys_button_text.font = "fonts/OpenDyslexic-Regular.otf"
    
        # here are the strings/numbers/booleans!
    def checkDefaultFont():
        if(persistent.useDyslexic == True):
            return "fonts/OpenDyslexic-Regular.otf"
        else:
            return "fonts/calibri.ttf"

    def checkUserDev():
        if(persistent.amDev == True):
            return True
        else:
            return False

    def checkSizeTwo():
        if(persistent.useDyslexic == True):
            return 13
        else:
            return 24

    def checkDefaultSize():
        if(persistent.useDyslexic == True):
            return dyslexic_size
        else:
            return normal_size

#####
# Label name: dyslexic
# 
# Description: Changes the default font and reloads the script if need be.
# 
# Parameters: none
# 
# Returns: none
#####
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