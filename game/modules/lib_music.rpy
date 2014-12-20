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
#     doublespeak Character() Character() String
# --or--
#     doublespeak Character() Character() String String
# --also--
#     /lib_music/music.txt holds entries for actual music for the music room
#     /lib_music/fakesfx.txt holds entries for sfx that are played like music
#     /lib_music/realsfx.txt holds entries for sfx
#######

init -1:
        # redundant but not show anything playing by default.
    $ playing = "Nothing"

init python:
    import os #abspath(), #isfile()
    from itertools import izip
    
    #####
    # Function name: dualwise()
    # 
    # Descripiton: Transforms data into tuplets of two (well three including garbage).
    # For looping sfx.
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
    # Descripiton: Transforms data into tuplets of three (well four including garbage).
    # For real sfx.
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
    # Descripiton: Transforms data into tuplets of four (well five including garbage).
    # For music.
    # 
    # Parameters:
    # iterable - the data
    # 
    # Returns: the transformed data
    #####
    def quadwise(iterable):
        list = iter(iterable)
        return izip(list, list, list, list, list)
    
    # Step 1. Find and parse the files for music.
    musicEntries = []
    mlib = os.path.abspath(config.gamedir + "/lib_music/music.txt")
    mlib = file(mlib).read().decode("utf-8")
    mlib = mlib.split("\n")
    for shortname, fileloc, longname, unlocked, nothing in quadwise(mlib):
        if(unlocked == "True"):
            unlocked = True
        else:
            unlocked = False
        newLine = (shortname, fileloc, longname, unlocked)
        musicEntries.append(newLine)
    
    # Step 2. Find and parse the files for sfx.
    sfxEntries1 = []
    sfxlib1 = os.path.abspath(config.gamedir + "/lib_music/fakesfx.txt")
    sfxlib1 = file(sfxlib1).read().decode("utf-8")
    sfxlib1 = sfxlib1.split("\n")
    for shortname, fileloc, nothing in dualwise(sfxlib1):
        newLine = (shortname, fileloc)
        sfxEntries1.append(newLine)
    sfxEntries2 = []
    sfxlib2 = os.path.abspath(config.gamedir + "/lib_music/realsfx.txt")
    sfxlib2 = file(sfxlib2).read().decode("utf-8")
    sfxlib2 = sfxlib2.split("\n")
    for shortname, fileloc, pause, nothing in tripwise(sfxlib2):
        if(pause == "True"):
            pause = True
        else:
            pause = False
        newLine = (shortname, fileloc, pause)
        sfxEntries2.append(newLine)
    
    # Step 3. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)
    
    # Step 4. Add music files.
    for entry in musicEntries:
        mr.add(entry[1], always_unlocked=entry[3])
    
    #####
    # Function name: mlib()
    # 
    # Descripiton: Plays music/sfx based on the shortcode.
    # 
    # Parameters:
    # selection - the shortcode
    # 
    # Returns: None
    #####
    # Step 5. Be able to run the music files.
    def mlib(selection):
        #bgm
        for entry in musicEntries:
            if(selection == entry[0]):
                renpy.music.play(entry[1], loop=True, fadein=1.0)
                break
        
        for entry in sfxEntries1:
            if(selection == entry[0]):
                renpy.music.play(entry[1], loop=True)
                break
            
        #sfxs
        for entry in sfxEntries2:
            if(selection == entry[0]):
                renpy.sound.play(entry[1])
                if(entry[2]):
                    renpy.pause(2.0)
                break
        return

    #####
    # Function name: name_playing()
    # 
    # Descripiton: Finds the name of the playing file.
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
        for entry in musicEntries:
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
        for entry in musicEntries:
            textbutton entry[2] action (SetVariable('playing', name_playing()), mr.Play(entry[1]))
        null height 20

        # Buttons that let us advance tracks.
        text "Now playing:\n[playing]\n"
        # research done - we need to change the variable before we move on
        # so that the callback works
        textbutton "Next" action (SetVariable('playing', name_playing()), mr.Next())
        textbutton "Previous" action (SetVariable('playing', name_playing()), mr.Previous())
        null height 20

        # The button that lets the user exit the music room.
        textbutton "Main Menu" action ShowMenu("main_menu")

    # Start the music playing on entry to the music room.
    #on "replace" action (mr.Play(), SetVariable('playing', name_playing()))

    # Restore the main menu music upon leaving.
    #on "replaced" action Play("music", "track1.ogg")
    