#these are additional functions meant for, to some extent, allowing font
#files and sizes to be directly selected by screens if need be. In other words, 
#we are hiding some of our hidden magic numbers here. (largely with recards 
#to the dyslexic options)

init -1 python:
    def checkDefaultFont():
        if (persistent.useDyslexic == True):
            return "OpenDyslexic-Regular.otf"
        else:
            return "calibri.ttf"

    def checkUserDev():
        if (persistent.amDev == True):
            return True
        else:
            return False

    def checkDefaultSize():
        if (persistent.useDyslexic == True):
            return 16
        else:
            return 26