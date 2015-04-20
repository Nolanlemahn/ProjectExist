#######
# File name: lib_music.rpy
# 
# Description: Dynamically declare music files
# 
# Original author: Nolan/NintendoToad
# 
# Type: Library, Screen
# 
# Usage:
#     # This is done for you!
#     $ mlib = mlib_space()
#     $ mlib.load()
#     # This isn't!
#     $ mlib(String) # This actually plays the music file in the correct channel
#                    # String is the song's shortcode
# --also--
#     /lib_music/music.txt holds entries for actual music for the music room
#     /lib_music/fakesfx.txt holds entries for sfx that are played like music
#     /lib_music/realsfx.txt holds entries for sfx
#######

init -1:
        # redundant but not show anything playing by default.
    $ playing = "Nothing"
    $ mlib_debug_key = "M"

init python:
    import os #abspath(), #isfile()
    import ast #literal_eval()
    from itertools import izip
    
    #####
    # Function name: dualwise()
    # 
    # Description: Transforms data into tuplets of two (well three including 
    # garbage). For looping sfx.
    # 
    # Parameters:
    # iterable - the data
    # 
    # Returns: the transformed data
    #####
    def dualwise(iterable):
        list = iter(iterable)
        return izip(list, list, list)
    
    
    #####
    # Function name: tripwise()
    # 
    # Description: Transforms data into tuplets of three (well four including 
    # garbage). For real sfx.
    # 
    # Parameters:
    # iterable - the data
    # 
    # Returns: the transformed data
    #####
    def tripwise(iterable):
        list = iter(iterable)
        return izip(list, list, list, list)
    
    
    #####
    # Function name: quadwise()
    # 
    # Description: Transforms data into tuplets of four (well five including 
    # garbage). For music.
    # 
    # Parameters:
    # iterable - the data
    # 
    # Returns: the transformed data
    #####
    def quadwise(iterable):
        list = iter(iterable)
        return izip(list, list, list, list, list)

    
    # Create a MusicRoom instance, and track mlib usage.
    mr = MusicRoom(fadeout=1.0)
    mlib_usage = 0
    
    #####
    # Class name: mlib()
    # 
    # Description: Plays music/sfx based on the shortcode.
    # 
    # Parameters:
    # selection - the shortcode
    # 
    # Returns: None
    #####
    # Step 5. Be able to run the music files.
    class mlib_space():
        def __init__(self, selection=""):
            global mlib_usage
            mlib_usage += 1
            if(mlib_usage > 1):
                renpy.error('more than one mlib object in use, only use one')
            self.selection = selection
            self.musicEntries = []
            self.sfxEntries1 = []
            self.sfxEntries2 = []
            self.data = []
            self.human_view = ""
            self.human_mute = False

        #####
        # Function name: __call__()
        # 
        # Description: Plays the specified music.
        # 
        # Parameters:
        # selection - the shortcode for the audio file we play
        # 
        # Returns: None
        #####
        def __call__(self, selection):
            #bgm
            for entry in self.musicEntries:
                if(selection == entry[0]):
                    self.data = entry
                    renpy.music.play(entry[1], loop=True, fadein=1.0)
                    return
            
            for entry in self.sfxEntries1:
                if(selection == entry[0]):
                    self.data = entry
                    renpy.music.play(entry[1], loop=True)
                    return
                
            #sfxs
            for entry in self.sfxEntries2:
                if(selection == entry[0]):
                    renpy.sound.play(entry[1])
                    if(entry[2] != 0):
                        renpy.pause(entry[2])
                    return
            return #nothing happened, oh well

        #####
        # Function name: load()
        # 
        # Description: Grabs data from the three text files, and sends it to the
        # Music Room, which we rebuild.
        # 
        # Returns: None
        #####
        def load(self): # load() should work like reload()
            # Step 1. Find and parse the files for music.
            self.musicEntries = []
            mlib_data = os.path.abspath(config.gamedir + "/lib_music/music.txt")
            mlib_data = file(mlib_data).read().decode("utf-8")
            mlib_data = mlib_data.split("\n")
            for shortname, fileloc, longname, unlocked, nothing in quadwise(mlib_data):
                if(unlocked == "True" or unlocked == "Unlocked"):
                    unlocked = True
                else:
                    unlocked = False
                newLine = (shortname, fileloc, longname, unlocked)
                self.musicEntries.append(newLine)
            
            # Step 2. Rebuild MusicRoom instance with our music
            global mr
            mr = MusicRoom(fadeout=1.0)
            for entry in self.musicEntries:
                mr.add(entry[1], always_unlocked=entry[3])
                
            # Step 3. Find and parse the files for sfx.
            self.sfxEntries1 = []
            sfxlib1 = os.path.abspath(config.gamedir + "/lib_music/fakesfx.txt")
            sfxlib1 = file(sfxlib1).read().decode("utf-8")
            sfxlib1 = sfxlib1.split("\n")
            for shortname, fileloc, nothing in dualwise(sfxlib1):
                newLine = (shortname, fileloc)
                self.sfxEntries1.append(newLine)
            self.sfxEntries2 = []
            sfxlib2 = os.path.abspath(config.gamedir + "/lib_music/realsfx.txt")
            sfxlib2 = file(sfxlib2).read().decode("utf-8")
            sfxlib2 = sfxlib2.split("\n")
            for shortname, fileloc, time, nothing in tripwise(sfxlib2):
                time = ast.literal_eval(time)
                newLine = (shortname, fileloc, time)
                self.sfxEntries2.append(newLine)
            return

        #####
        # Function name: get_playing()
        # 
        # Description: Gets a string representing the song that's playing in a 
        # sane manner.
        # 
        # Parameters:
        # showScreen - Put the data on the screen.
        # 
        # Returns: the transformed data
        # 
        # Format: [march] - <Title - Artist> - (File Location)
        #####
        def get_playing(self, showScreen = True):
            entry = self.data
            store.mlib_timer = 1.0
            try:
                self.human_view = "<" + entry[2] + ">"
                if config.developer:
                    self.human_view = "["+ entry[0] +"] - " + self.human_view +  "- (" + entry[1] + ")"
            except:
                self.human_view = "[Nothing is playing]"
            if(showScreen):
                renpy.call_in_new_context("mlib_show_data")
            return self.human_view

        def silence(self, seconds=2.0):
            renpy.music.set_volume(0.0, seconds, channel="music")
            return
        def unsilence(self, seconds=2.0):
            if(not self.human_mute):
                renpy.music.set_volume(1.0, seconds, channel="music")
            return
        def stop(self, time=None):
            renpy.music.stop(channel='music', fadeout=time)
            self.data = []
            return
        def ui_mute(self):
            if(not self.human_mute):
                self.human_mute = True
                renpy.music.set_volume(0.0, 2.0, channel="music")
            else:
                self.human_mute = False
                renpy.music.set_volume(1.0, 2.0, channel="music")
            return
        def restart(self):
            if(renpy.music.get_playing()):
                renpy.music.play(renpy.music.get_playing(), loop=True, fadein=1.0)
            return

label mlib_show_data:
    scene black
    show text "[mlib.human_view]" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    return

init:
    $ mlib = mlib_space()
    #$ break_renpy = mlib_space()
    $ mlib.load()
    
init python:
    #####
    # Function name: name_playing()
    # 
    # Description: Finds the name of the playing file.
    # 
    # Parameters:
    # selection - the shortcode
    # 
    # Returns: The author-given name.
    #####
    # Step 6. Be able to look up names.
    def name_playing():
            # be ready to realize that we might not find the song
        never_seeked = True
        file_playing = renpy.music.get_playing()
            # seek only through the music
        for entry in mlib.musicEntries:
            if(file_playing == entry[1]):
                file_playing = entry[2]
                never_seeked = False
                break
            
        if(never_seeked):#handle none case
            file_playing = "Nothing"
            # manually update store.playing just in case
        if(hasattr(store, 'playing')):
            store.playing = file_playing
        return file_playing
    config.python_callbacks.append(name_playing)

# Step 7. Create the music room screen.
screen music_room:

    tag menu
    window:
        style "mm_root"#background
    frame:
        has vbox

        # The buttons that play each track.
        for entry in mlib.musicEntries:
            textbutton entry[2] action (SetVariable('playing', name_playing()), mr.Play(entry[1]))
        null height 20

        # Buttons that let us advance tracks.
        text "Now playing:\n[playing]\n"
        # research done - we need to change the variable before we move on
        # so that the callback works
        textbutton "Next" action (SetVariable('playing', name_playing()), mr.Next())
        textbutton "Previous" action (SetVariable('playing', name_playing()), mr.Previous())
        textbutton "Stop" action (SetVariable('playing', "Nothing"), Function(mlib.stop, 1.0))
        null height 20

        # The button that lets the user exit the music room.
        textbutton "Main Menu" action ShowMenu("main_menu")

    # Start the music playing on entry to the music room.
    #on "replace" action (mr.Play(), SetVariable('playing', name_playing()))

    # Restore the main menu music upon leaving.
    #on "replaced" action Play("music", "track1.ogg")
    
# Make label start show this
screen mlib_listener:
    key mlib_debug_key action Show("mlib_debug")
    
screen mlib_debug:
    tag mlib
    modal True
    $ mlib
    $ mlib_viewable = mlib.get_playing(showScreen = False)
    frame:
        align (.025, .5)
        has vbox
        if(config.developer):
            label "mlib Debug Menu"
        else:
            label "Music Library Controls"
        textbutton "Restart Song" action Function(mlib.restart)
        textbutton "Mute/Unmute Music" action Function(mlib.ui_mute)
        #textbutton "What's Playing" action Function(mlib.get_playing)
        textbutton "Return" action Hide("mlib_debug")
    frame:
        align (0.025, 0.4)
        text "[mlib_viewable]"