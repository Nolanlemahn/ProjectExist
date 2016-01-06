label draft1:
    scene bg blackdrop
    $ clock = False
    $ walletshow = False
    scentered "Draft 1: ???"
    $ clock = True
    $ walletshow = True
    $ mlib("march")
    scene bg fakefog
    with dissolve
    scene bg fog
    nnvlmc "I'm aware of the power within my body. Not because I am innately 
            powerful, but because I have mastered the art of claiming that I 
            have power."
    nnvlmc "This is why I wished that I was not born a human. Our lust for that 
            which we do not have... It's one I could not control. And it is no 
            longer possible to make amends with those that I brought down with 
            me."

    nnvlmc "These once-white hands of mine seized what their master wanted by 
            force, and now they are stained with blood. Nothing will reverse the
            harm that they've done. I have bent this world to my will."
    nnvlmc "The girl that I thought would make me happy. The money that I 
            thought would save my home. The blade that killed my father. All 
            of these I sought to satiate my desires, simply because I could."

    nnvlmc "I lived out those fantasies in my dreams so that they could take 
            place in reality. Not fantasies of domination, but fantasies of... 
            having what I wanted. But that in itself is a display of power."

    nnvlmc "The world cheered as I remove its threats, but I am no savior. I 
            am simply - as I always have - keeping up my appearances. It didn't 
            know what I was doing when it wasn't looking, or why I was helping 
            its inhabitants."
    nnvlmc "I have bent this world to my will, and I have given into my shadow. 
            But he is silent. So whose nightmare is this, really? Mine because 
            of what I have done, or my Dream Guide's because of what she's 
            seen?"
    nnvlmc "Perhaps it doesn't matter. Perhaps all I need to do is wait for my 
            life to end..."
    return

label draft2:
    scene bg blackdrop
    $ clock = False
    $ walletshow = False
    scentered "Draft 2: The Chase"
    $ clock = True
    $ walletshow = True
    $ mlib("march")
    $ sio_l("bg fakefog")
    scene bg fog
    nvln "Officer Ryan rams the gearstick into drive and stares down the road, as 
          if the road is a rabid dog to be pacified."
    nvlry "Move, you piece of shit."
    nvln "Ryan didn't have time to read through the file. No one did. The call for 
          immediate request and detain had only gone out 30 seconds ago. In fact, 
          Ryan was in the middle of a coffee break."
    nvlry "Selena, who the hell is this kid?"
    nvlse "Kazuki Kamata. Age 18. Short black hair. Lanky. Unusual display of physical 
           ability. Do not shoot for any reason."
    nvln "Ryan's car grumbles to a start."
    nvlry "Unusual display of physical ability? How unusual?"
    nvlse "Umm. Parkour, surviving a 300-feet drop...{nw}"
    nvlry "Please. Don't you remember that one story about that one woman that fell 
           out of an airplane?"
    nvlse "This kid was running at 25 miles an hour after the fall."
    nvlry "... The fuck? That's almost as fast as Usain Bolt..."
    nvlse "No, you don't understand. Kazuki ran at that pace for a solid 5 minutes."
    nvlry "Where was he last spotted?"
    nvlse "Corner of 5th and G."
    nvln "Ryan jabs at his GPS, setting a route for G Street."
    nvlry "Anyone else on his tail? Or catch him on CCTV?"
    nvlse "The 5th and G sighting was on CCTV."
    nvl clear
    nvlry "How long ago was that?"
    nvlse "2 minutes ago now."
    nvlry "Anyone tag him?"
    nvlse "No."
    nvlry "Shit."
    nvlse "Yeah. Get moving. Assume that he's armed and dangerous... especially if you 
           don't see any weapons."
    nvl clear
    $ sio_l("bg fakefog")
    scene bg fog
    nnvlmc "It burns."
    return
