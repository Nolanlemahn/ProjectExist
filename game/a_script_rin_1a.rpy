# Aborted Arc + Schrödinger's Gun much? This'll be a crapload of fun.
label Rin_1a:#this_label_done
    call rollfind
    $ mother_name = "Mother"
    $ shadow_name = "Rin's Shadow"
    $ main_name = "?"
    $ main_type = "kf"
    $ main_char_level = 5
    # start implementing the table of stats
    $ main_char_maxHP = 100
    $ main_char_currentHP = 100
    $ main_char_maxBelly = 100
    $ main_char_currentBelly = 100
    $ main_char_maxSleep = 400
    $ main_char_currentSleep = 350
    $ main_char_maxXP = 50
    $ main_char_currentXP = 0
    $ main_char_stats = [20,20,20,20,20,20]
    # STR, DEX, RES, SPD, INT, SPI
    $ main_char_ABI_SLO1 = "No ability"
    $ main_char_ABI_SLOL1 = 0
    $ main_char_ABI_SLO2 = "No ability"
    $ main_char_ABI_SLOL2 = 0
    $ main_char_RS_SLO1 = "No symbol"
    $ main_char_RS_SLOL1 = 0
    $ main_char_RS_SLO2 = "No symbol"
    $ main_char_RS_SLOL2 = 0
    $ main_char_weapon = "Fists"
    $ main_char_armor = "Nothing"
    $ main_known_moves = [1,2,0,0,0,0]
    
    $ j_name = "???"
    #[needed for clocks
    $ theweekday = 3#tuesday
    $ themonth = 9
    $ theday = 21
    $ theyear = 2010
    $ dayofyear = 264
    $ yearlim = 365
    $ daylim = 30
    $ stringweekday = "Tuesday"
    $ stringmonth = "September"    
    $ main_char_cash = 200.00
    $ has_phone = False
    #]
    
    $ walletshow = True
    $ main_char_show_rpg = True
    $ clock = True
    $ change = False
    $ strchange = ""
    $ progress = "000"
    
    ###########
    
    #Jonathan
    $ j = DynamicCharacter("j_name", color="#ADD8E6", kind=char_blue, show_two_window=True)
    $ nvlj = Character('Johnathan', color="#ADD8E6", kind=nvl_blue)
    
    #Kazuki
    $ k = Character("Kazuki", color="#C0C0C0", kind=char_gray, show_two_window=True)#standardmain
    $ nvlk = DynamicCharacter("main_name", color="#C0C0C0", kind=nvl_gray)#nvlmain
    $ nk = Character(None, what_style="main_gray")#thinkmain
    $ nnvlk = Character(None, color="#C0C0C0", kind=nvl_gray)#nvl-thinkmain
    
    #Rin
    $ mc = Character("Rin", color="#C0C0C0", kind=char_gray, show_two_window=True)
    $ nmc = Character(None, color="#C0C0C0", kind=char_gray)
    $ nvlmc = Character("Rin", color="#C0C0C0", kind=nvl_gray, who_suffix = ":")
    $ nvlnmc = Character(None, color="#C0C0C0", kind=nvl_gray)
    
    #Rin's Mother
    $ rm = DynamicCharacter("mother_name", color="#FFFFFF", kind=char_white)
    $ nvlrm = DynamicCharacter("mother_name", color="#FFFFFF", kind=nvl_white, who_suffix = ":")
    
    #Shadow
    $ s = DynamicCharacter("shadow_name", color="#C0C0C0", kind=char_gray, show_two_window=True)
    $ nvls = DynamicCharacter("shadow_name", color="#C0C0C0", kind=nvl_gray, who_suffix = ':')
    
    $ minutes = 360
    $ clock = True

    
label Rin_1b:
    show screen button
    #ui.button("surprise")
    #Help("www.google.com")
    scene bg fakefog
    with dissolve
    scene bg fog
    
    #[scene1
    $ mlib("room3")
    $ dev_screen = "pass"
    nvlnmc "Katherine. Because it was my mother's mother's name."
    nvlnmc "Rin. Because I didn't want to be German."
    nvlnmc "Faust. Because it was the name on the back of the photo left with me."
    nvlnmc "Katherine \"Rin\" Faust. Abandoned. Unwanted. Left behind. Me."
    nvlnmc "Some say my parents abandoned me because I was the unplanned result of a honeymoon. Some say they wanted a boy. Some say I was assumed to be defunct, since I made no sounds."
    nvlnmc "It doesn't matter. Speculation doesn't matter. Only the truth matters."
    nvlnmc "And the truth is that this world is filled with both light and darkness. I was born into darkness."
    nvl clear
    
    nvlrm "Katherine!"
    nvlmc "It's \"Rin\", Mother."
    nvlrm "... Rin, what are you doing?"
    nvlmc "That should be obvious. Burning my past. This photo, this blanket. They are both useless, now."
    nvlrm "They aren't useless! Those are... were mementos of your parents."
    nvlmc "My parents left me here. They don't want to remember me; I should not remember them."
    nvlrm "But... they... Rin, you're burning your arm!"
    nvlnmc "I am reliving a day from when I was 8. The date doesn't matter. This is a dream.{w}\nI walk over to the sink, and run my right arm under the cold water."
    nvlrm "We need to get you to the ER! Rin, I can't afford another trip to the hospital!"
    nvlmc "... My arm is fine, Mother. My arm doesn't matter."
    nvlnmc "Mother backs away from me. Pain is a concept for her. It isn't for me; it never was.{w}\nI place the ashes of the photo and blanket in a plastic earring pouch. The pouch sits in my back pocket to this day."
    nvlrm "... Rin..."
    nvlnmc "I ignore her, and go to my desk to resume studying."
    extend "\nOr at least, I do in my dream. Out here, I sigh, and sit down, and broadcast my demand."
    nvlmc "Well. I've been having that dream for the past 16 years. Show me something different."
    nvlnmc "And then I let myself fall into my dream..."
    nvl clear
    
    $ mlib("march")
    nvls "Stand."
    nvlnmc "I stand up, staring my shadow straight in the blue void that represents its eye. I know that it is my shadow. I know that it is a reflection of humanity, and wishes me to give into my carnal instincts. But I also know that it is dangerous, as neither of us yet understand the other."
    nvls "Feel pain. Remember me."
    nvlnmc "My shadow begins to shake rapidly, giving the appearance of transparency. But it can't hide from me.{w}\nI extend my right arm, catching my shadow's own right arm before his hand connects with my stomach."
    nvlnmc "Its blue voids widen in surprise acknowledging that I am both hostile and interested."
    nvlmc "I am above you, shadow."
    nvls "..."
    nvlnmc "My shadow flings me several hundred miles away. I feel my skin ripple as I hurtle through space."
    extend "\nI see a wall coming up ahead. I smash my hands and feet into it, taking a catlike stance on the wall."
    nvlnmc "I examine my body. Other than slight burn marks on my hands, I am completely unharmed."
    nvlmc "That is not how pain works."
    nvlnmc "I channel energy through both of my hands."
    nvl clear
    
    $ persistent.seen_move[3] = 1
    nmc "... Warlock's Fists. I pull energy from the world around me, and launch myself towards my shadow, pummeling it all the while."
    $ persistent.seen_move[4] = 1
    nmc "... Hell's Breeze. My shadow leaps backwards, leaving a multitude of meteors behind. But I plow directly through them, as if they did not exist."
    nmc "My shadow raises its hands in surrender. That is because I am holding my shadow by its neck, and standing over the void."
    mc "... Pain is the body's acknowledgement of fear. Fear is the understanding that you are no longer are in control of your own destiny. You fear me, and now you feel pain."
    s "... What are you?"
    nmc "My shadow has its own answer. It doesn't want to know the actual answer. It simply wants to know what I consider myself to be."
    mc "Just a girl who perfectly understands darkness, and therefore perfectly understands this world."
    s "... No. You are darkness. Compared to you, I am light."
    nmc "My shadow lets out a light chuckle, which builds into hearty laughter, which finally becomes a hyena's call."
    mc "... Annoying."
    nmc "I encase my shadow in diamonds before returning to the world of the living... "
    #should this be a menu?
    
    #define wrack at some point