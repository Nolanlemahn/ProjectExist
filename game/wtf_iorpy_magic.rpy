#        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                    Version 2, December 2004 
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 
#
# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

init python:
    try:
        import EasyDialogsWin as EasyDialogs
    except:
        EasyDialogs = None
    import re
    import os
    import subprocess
    import sys
    import platform
    import shutil
    dirname = "ProjectExist"#change this to something like your game name
    
    from os.path import expanduser
    home = expanduser("~")
    
    def begin_game():
        savename = renpy.input("Please name this savefile.")
        savename = savename.strip()
        valid = re.match('^[a-zA-Z0-9]+$', savename) is not None
        if(((savename == "") or (savename == None)) or not valid):
            renpy.say(None, "That savefile name was invalid. Please try again.")
            savename = begin_game()
        if not os.path.exists(home + "/My Games/" + dirname + "/" + savename):
            try:
                os.makedirs(home + "/My Games/" + dirname + "/" + savename)
                #renpy.say(None, "A folder now exists at \"" + (os.path.abspath(home + "/My Games/" + dirname + "/" + savename)) + 
                #    "\". This is a beta feature. Please do not delete it.")
            except:
                renpy.say(None, "It appears that you do not have permission to write to your own folder. Remedy this before playing " + 
                    build.executable_name + ".")
                renpy.reload_script()
        else:
            renpy.say(None, "That savefile name has already been taken. Please choose a different one.")
            savename = begin_game()
        renpy.take_screenshot()
        renpy.save(savename, savename)
        return savename
    
    def get_user_dir():
        return (home + "/My Games/" + dirname + "/" + store.save_name)
    
    #below functions require $ save_name = begin_game() somewhere in label start
    def create_file(magic_folder, magic_file):
        if(magic_folder == None):
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_file)
        else:
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_folder + "/" + magic_file)
        file = open(magic_file, 'w+')
        file.close()
        return
        
    def delete_file(magic_folder, magic_file):#DANGEROUSDANGEROUSDANGEROUS
        if(magic_folder == None):
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_file)
        else:
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_folder + "/" + magic_file)
        # Written by Thorium
        try:
            os.remove(magic_file)
        except:
            renpy.say(None, "You do not appear to have the adequate permissions required to delete this folder" + build.executable_name + ".")
        #
        return
    
    def stringify_file(magic_folder, magic_file):
        if(magic_folder == None):
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_file)
        else:
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_folder + "/" + magic_file)
        #Written by Thorium
        str = ""
        try:
            file = open(magic_file, 'r+')#needed single quote
            str = file.read().decode("utf-8")
            file.close()
        except:
            renpy.say(None, "It appears the file you're attempting to access is unreadable, please remedy this" + build.executable_name + ".")
        return str
        #
        #return file(magic_file).read().decode("utf-8")
    
    def filify_string(given_message, magic_folder, magic_file):
        if(magic_folder == None):
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_file)
        else:
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_folder + "/" + magic_file)
        #Written by Thorium
        try: 
            file = open(magic_file, 'w+')
            file.write("%s" % given_message)
            file.close()
        except: 
            renpy.say(None, "It appears that you are unable to write to this file, please remedy this." + build.executable_name)
        #
        return
    
    def create_folder(magic_folder):
        magic_folder = os.path.abspath(get_user_dir() + "/" + magic_folder)
        if not os.path.exists(magic_folder):
            try:
                os.makedirs(magic_folder)
            except:
                renpy.say(None, "It appears that you do not have permission to write to your own folder. Remedy this before playing " + 
                    build.executable_name + ".")
                renpy.reload_script()
        return
        
    def delete_folder(magic_folder):#DANGEROUSDANGEROUSDANGEROUS
        magic_folder = os.path.abspath(get_user_dir() + "/" + magic_folder)
        #Written by Thorium
        try:
            shutil.rmtree(magic_folder)
        except:
            renpy.say(None, "You do not appear to have the adequate permissions required to delete this folder" + build.executable_name + ".")
        #
        return
    
    def show_file(magic_folder, magic_file):
        if(magic_folder == None):
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_file)
        else:
            magic_file = os.path.abspath(get_user_dir() + "/" + magic_folder + "/" + magic_file)
        #Written by Thorium
        try:
            if sys.platform == "win32":
                os.startfile(magic_file)
            elif platform.mac_ver()[0]:
                subprocess.Popen([ "open", magic_file ])
            else:
                subprocess.Popen([ "xdg-open", magic_file ])
        except: 
            renpy.say(None, "It appears the file you're attempting to access is unreadable, please remedy this." + build.executable_name)
        #
        return
        
    def show_folder(magic_folder):
        magic_folder = os.path.abspath(get_user_dir() + "/" + magic_folder)
        #Written by Thorium
        try:
            if sys.platform == "win32":
                os.startfile(magic_folder)
            elif platform.mac_ver()[0]:
                subprocess.Popen([ "open", magic_folder ])
            else:
                subprocess.Popen([ "xdg-open", magic_folder ])
        except: 
            renpy.say(None, "The folder you're trying to open appears unreadable, please remedy this." + build.executable_name)
        #
        return
    
    def ui_find_folder(given_message, magic_folder):
        magic_folder = os.path.abspath(get_user_dir() + "/" + magic_folder)
        if EasyDialogs:
            choice = EasyDialogs.AskFolder(message="%s"%given_message, defaultLocation=renpy.fsencode(magic_folder), wanted=unicode)
            if choice is not None:
                path = choice
            else:
                path = None
        else:
            cmd = [ "/usr/bin/python", os.path.join(config.gamedir, "tkaskdir.py"), 
                renpy.fsencode(config.gamedir + "/" + magic_folder), given_message ]
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            choice = p.stdout.read()
            code = p.wait()
        return choice
    
    def ui_find_file(given_message, magic_folder):
        magic_folder = os.path.abspath(get_user_dir() + "/" + magic_folder)
        if EasyDialogs:
            choice = EasyDialogs.AskFileForOpen(message="%s"%given_message, defaultLocation=renpy.fsencode(magic_folder), wanted=unicode)
            if choice is not None:
                path = choice
            else:
                path = None
        else:
            cmd = [ "/usr/bin/python", os.path.join(config.gamedir, "tkaskfile.py"), 
                renpy.fsencode(magic_folder), given_message ]
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            choice = p.stdout.read()
            code = p.wait()
        return choice
        
    def kill_save(savename):
        shutil.rmtree(os.path.abspath(home + "/My Games/" + dirname + "/" + savename))
        return
        
    def freaking_delete_every_external_file_associated_with_this():
        try:
            shutil.rmtree(os.path.abspath(home + "/My Games/" + dirname))
            shutil.rmtree(os.path.abspath(config.savedir))
        except:
            renpy.say(None, "We were unable to delete things.")
        return
        
label reset_button:
    $ freaking_delete_every_external_file_associated_with_this()
    return
    
label test_iorpy_magic:
    $ save_name = begin_game()
    $ create_folder("homework")
    $ ui_find_file("hiya", "homework")
    $ create_file("homework", "assignment1.txt")
    $ show_file("homework", "assignment1.txt")
    "Pausing so you can see the new file. Please close the file."
    $ filify_string("line1\nline2\nbaked bread", "homework", "assignment1.txt")
    $ show_file("homework", "assignment1.txt")
    "Pausing so you can see the new file. Please close the file."
    $ delete_file("homework", "assignment1.txt")
    $ delete_folder("homework")
    $ create_folder("homework")
    $ kill_save(save_name)
    return
#v0.1.2 changelog from v0.1.1
#Throium made marked functions safer
#actual alphanumeric check

#v0.1.1 changelog from v0.1.0
#begin_game() is more thorough
#really added
#filify_string(given_message, magic_folder, magic_file):
#kill_save(savename):
#freaking_delete_every_external_file_associated_with_this():