init python:
    def mlib(selection):
        #bgm
        if(selection == "room3"):
            renpy.music.play("bgm/room3.mp3", loop=True, fadein=1.0)
        if(selection == "round"):
            renpy.music.play("bgm/the_round.mp3", loop=True, fadein=1.0)
            
        #these sfxs act as bgm, but do not constitute "music" in their own rights
        #as such, we will not mark them as unlocked
        if(selection == "march"):
            renpy.music.play("bgm/march.mp3", loop=True)
        if(selection == "calarm"):
            renpy.music.play("sfx/clock_alarm.wav", loop=True)
        if(selection == "falarm"):
            renpy.music.play("sfx/domestic_falarm.mp3", loop=True)
            
        #sfxs
        if(selection == "cskid"):
            renpy.sound.play("sfx/car_skid.mp3")
            renpy.pause(2.0)
        return
        
        
# MusicRoom code #
init python:
    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)
    # Step 2. Add music files.
    mr.add("bgm/room3.mp3", always_unlocked=True)
    mr.add("bgm/the_round.mp3", always_unlocked=True)
    mr.add("bgm/march.mp3", always_unlocked=True)
    mr.add("bgm/march2.mp3", always_unlocked=True)
    # Step X. name lookup
    
    def name_playing():
        file_playing = renpy.music.get_playing()
        if(file_playing == "bgm/room3.mp3"):
            file_playing =  "Room 3 - AgentAbacus"
        elif(file_playing == "bgm/the_round.mp3"):
            file_playing =  "The Round - Nihilore"
        elif(file_playing == "bgm/march.mp3"):
            file_playing =  "The Shadow's March - AgentAbacus"
        elif(file_playing == "bgm/march2.mp3"):
            file_playing =  "Lawrence's Reveal - AgentAbacus"
            
        elif(file_playing == None):#handle none case
            file_playing = "Nothing"
        else:#handle otherwise unhandled file
            file_playing =  "Secret file!"
        if (hasattr(store, 'playing')):
            store.playing = file_playing
        return file_playing
    config.python_callbacks.append(name_playing)

# Step 3. Create the music room screen.
screen music_room:

    tag menu
    window:
        style "mm_root"#background
    frame:
        has vbox

        # The buttons that play each track.
        textbutton "Room 3 - AgentAbacus" action (mr.Play("bgm/room3.mp3"), SetVariable('playing', name_playing()))
        textbutton "The Round - Nihilore" action (mr.Play("bgm/the_round.mp3"), SetVariable('playing', name_playing()))
        textbutton "The Shadow's March - AgentAbacus" action (mr.Play("bgm/march.mp3"), SetVariable('playing', name_playing()))
        textbutton "Lawrence's Reveal - AgentAbacus" action (mr.Play("bgm/march2.mp3"), SetVariable('playing', name_playing()))
        null height 20

        # Buttons that let us advance tracks.
        text "Now playing:\n[playing]\n"
        # now playing doesn't work without setting store.playing twice. research?
        textbutton "Next" action (mr.Next(), SetVariable('playing', name_playing()))
        textbutton "Previous" action (mr.Previous(), SetVariable('playing', name_playing()))
        null height 20

        # The button that lets the user exit the music room.
        textbutton "Main Menu" action ShowMenu("main_menu")

    # Start the music playing on entry to the music room.
    #on "replace" action (mr.Play(), SetVariable('playing', name_playing()))

    # Restore the main menu music upon leaving.
    #on "replaced" action Play("music", "track1.ogg")
    