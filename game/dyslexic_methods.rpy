init -1 python hide:
    
    def checkFont():
        if (persistent.useDyslexic == True):
            return "OpenDyslexic-Regular.otf"
        else:
            return "calibri.ttf"
    
    def checkDev():
        if (persistent.amDev == True):
            return True
        else:
            return False
    
    def checkSize():
        if (persistent.useDyslexic == True):
            return 16
        else:
            return 26
            
    style.dys_button = Style(style.button_text)
    style.dys_button_text.font = "OpenDyslexic-Regular.otf"