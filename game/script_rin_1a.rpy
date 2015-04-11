# Aborted Arc + Schrödinger's Gun much? This'll be a crapload of fun.
label Rin_1a:#this_label_done
    
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
    $ answers = []
    
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
    
    $ etname = "English Teacher"
    $ et = DynamicCharacter("etname", show_two_window=True)
    
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
    $ mother_name = "Ariadne"
    $ rm = DynamicCharacter("mother_name", color="#FFFFFF", kind=char_white)
    $ nvlrm = DynamicCharacter("mother_name", color="#FFFFFF", kind=nvl_white, who_suffix = ":")
    
    #Shadow
    $ s = DynamicCharacter("shadow_name", color="#C0C0C0", kind=char_gray, show_two_window=True)
    $ nvls = DynamicCharacter("shadow_name", color="#C0C0C0", kind=nvl_gray, who_suffix = ':')
    
    $ minutes = 885
    $ clock = True
    jump Rin_1c
    
label Rin_1b:
    #ui.button("surprise")
    #Help("www.google.com")
    scene bg fakefog
    with dissolve
    scene bg fog
    
    #[scene1
    $ mlib("room3")
    nvlnmc "Katherine. Because it was my mother's mother's name."
    nvlnmc "Rin. Because I didn't want to be German."
    nvlnmc "Faust. Because it was the name on the back of the photo left with me."
    nvlnmc "Katherine \"Rin\" Faust. Abandoned. Unwanted. Left behind. Me."
    nvlnmc "Some say my parents abandoned me because I was the unplanned result 
            of a honeymoon. Some say they wanted a boy. Some say I was assumed 
            to be defunct, since I made no sounds."
    nvlnmc "It doesn't matter. Speculation doesn't matter. Only the truth 
            matters."
    nvlnmc "And the truth is that this world is filled with both light and 
            darkness. I was born into darkness."
    nvl clear
    
    nvlrm "Katherine!"
    nvlmc "It's \"Rin\", Mother."
    nvlrm "... Rin, what are you doing?"
    nvlmc "That should be obvious. Burning my past. This photo, this blanket. 
           They are both useless, now."
    nvlrm "They aren't useless! Those are... were mementos of your parents."
    nvlmc "My parents left me here. They don't want to remember me; I should not
           remember them."
    nvlrm "But... they... Rin, you're burning your arm!"
    nvlnmc "I am reliving a day from when I was 8. The date doesn't matter. This
            is a dream.{w}\nI walk over to the sink, and run my right arm under 
            the cold water."
    nvlrm "We need to get you to the ER! Rin, I can't afford another trip to the
           hospital!"
    nvlmc "... My arm is fine, Mother. My arm doesn't matter."
    nvlnmc "Mother backs away from me. Pain is a concept for her. It isn't for 
            me; it never was.{w}\nI place the ashes of the photo and blanket in 
            a plastic earring pouch. The pouch sits in my back pocket to this 
            day."
    nvlrm "... Rin..."
    nvlnmc "I ignore her, and go to my desk to resume studying."
    extend "\nOr at least, I do in my dream. Out here, I sigh, and sit down, 
            and broadcast my demand."
    nvlmc "Well. I've been having that dream for the past 16 years. Show me 
           something different."
    nvlnmc "And then I let myself fall into my dream..."
    nvl clear
    
    $ mlib("march")
    nvls "Stand."
    nvlnmc "I stand up, staring my shadow straight in the blue void that 
            represents its eye. I know that it is my shadow. I know that it is a
            reflection of humanity, and wishes me to give into my carnal
            instincts. But I already have."
    nvlnmc "I also know that it is dangerous, as neither of us yet understand 
            the other. At least, not fully."
    nvls "Feel pain. Remember me."
    nvlnmc "My shadow begins to shake rapidly, giving the appearance of 
            transparency. But it can't hide from me.{w}\nI extend my right arm, 
            catching my shadow's own right arm. His hand fails to connect with
            my stomach."
    nvlnmc "Its blue voids widen in surprise acknowledging that I am both
            hostile and interested."
    nvlmc "I am above you, shadow."
    nvls "..."
    nvlnmc "My shadow flings me several hundred miles away. I feel my skin 
            ripple as I hurtle through space."
    extend "\nI see a wall coming up ahead. I smash my hands and feet into it, 
            taking a catlike stance on the wall."
    nvlnmc "I examine my body. Other than slight burn marks on my hands, I am 
            completely unharmed."
    nvlmc "That is not how pain works."
    nvlnmc "I channel energy through both of my hands."
    nvl clear
    
    $ persistent.seen_move[3] = 1
    nmc "... Warlock's Fists. I pull energy from the world around me, and launch
         myself towards my shadow, pummeling it all the while."
    $ persistent.seen_move[4] = 1
    nmc "... Hell's Breeze. My shadow leaps backwards, leaving a multitude of 
         meteors behind. But I plow directly through them, as if they did not 
         exist."
    nmc "My shadow raises its hands in surrender. That is because I am holding 
         my shadow by its neck, and standing over the gaping hole that is my 
         heart."
    mc "... Pain is the body's acknowledgement of fear. Fear is the 
        understanding that you are no longer in control of your own destiny.
        You fear me, and now you feel pain."
    s "... What are you?"
    nmc "My shadow has its own answer. It doesn't want to know the actual 
         answer. It simply wants to know what I consider myself to be."
    mc "Just a girl who perfectly understands darkness, and therefore perfectly
        understands this world."
    s "... No. You are darkness. Compared to you, I am light."
    nmc "My shadow lets out a light chuckle, which builds into hearty laughter,
         which finally becomes a hyena's call."
    mc "... Annoying."
    nmc "I encase my shadow in diamonds before returning to the world of the
         living... "

label Rin_1c:
    et "Rin? Hey, Rin. I was asking you a question."
    mc "I don't care."
    nmc "I have several goals in life, but making my English instructor happy 
         doesn't happen to be one of them."
    et "Okay, look here Rin. Your participation in this class is part of your 
        grade. I'm sure that your mother wouldn't be happy if-"
    mc "Are you threatening me?"
    et "Ahh... No, I just-"
    mc "You were threatening me, and I don't appreciate that. And as long as I'm
        healthy, my mother doesn't care about my grades in the slightest."
    et "I'm not so sure..."
    mc "And also, the answer to your question is very simple, I'm not sure what 
        you'd gain from a student-provided answer. The author in that passage 
        was clearly trying to convey anger, but he wasn't doing it with his 
        word choice in the dialogue."
    et "Wait. What?"
    mc "It was the word choice in the description. \"And thusly, he began to 
        pace back and forth, with each step grinding more of the earth into the 
        flea-ridden ground, and clenching his fists tighter until his palms 
        began to bleed.\""
    mc "Not only are the character's actions gradually becoming more intense, 
        but they're certainly more effective than any of the preceding dialogue.
        \"The manner in which you wrote me off was simply unforgiveable.\""
    et "... I suppose."
    nmc "The English instructor had asked me what the author's goal was. I 
         suppose that, for once, I had forgotten to ensure that my physical 
         composure was that of an attentive student."
    nmc "Not that I wasn't attentive. I am perfectly capable of making myself 
         aware of the classroom while being engrossed within my own mind... 
         If I so choose, of course."
    nmc "Anyway... being encased in diamonds actually seems like an interesting 
         \"way to go\" for any being at all. It would certainly be a fitting -
         if not ironic - end for the citizens of such a materialistic city."
    $ minutes = minutes + 2
    mc "Does anyone happen to know where I could get twenty metric tons of 
        diamonds?"
    et "I was in the middle of going over... and respecting... your analysis. 
        Of all of the questions to interrupt me with... you chose that one?!"
    mc "Mmm. I felt that my question was more important."
    et "Anyway... If I did know where to get twenty fucking tons of diamond... 
        I wouldn't be teaching this shit."
    mc "Ah, excellent point. Never mind then. Continue. Oh, but you may be 
        getting a few phone calls tonight."
    et "About what?!"
    mc "Your interesting vocabulary choice."
    nmc "The instructor's outburst had garnered more than a few stares from 
         the listening students - some of which were likely not well-versed in 
         the explicit vernacular. Although that's likely a small number."
    "Boy" "Fucking? What's fucking?"
    "Girl" "I don't know. My parents were saying \"fuck you\" to each other last
            night, though."
    "Other Boy" "Fucking means that our teacher is in trooooooouble!"
    nmc "Most of the students, as I had guessed, were rolling their eyes, 
         snickering, or smirking. A few - maybe two - of the students seemed 
         genuinely confused."
    et "Gggk... Whatever. Class dismissed."
    nmc "Heh. That went far better than expected. I suppose that it would be 
         wise of the instructor to get liquored up before dealing with the 
         slew of malevolent students."
    nmc "Anyway, I had some digging to do, considering that I need to get my 
         hands on twenty tons of diamond."
    nmc "... Digging. Hmm. Wouldn't it be ironic if it turned out that they are 
         made in the Earth's crust, or something along those lines? Wait, why 
         don't I know?"
    nmc "Argh, our teachers don't teach us anything interesting..."
    nmc "It actually occurs to me that I could figuratively just pull hundreds 
         of tons of diamonds from my rear end, but now I'm actually curious 
         about this whole thing."
    nmc "Well, this class doesn't normally end until 3:20 PM, but thanks to that
         exceedingly amusing debacle, I get to head home early today. Yay!"
    
label Rin_1d:
    $ triple_min(10)
    mc "I'm home, Mother."
    rm "Oh, welcome ho- what? It's not even 3:20 PM yet."
    mc "I know, My English class ended early today."
    rm "This is the first time you've ever been home this early, though. What 
        happened?"
    mc "The English instructor wasn't feeling well. In fact, he said \"fuck\" or
        something like that."
    rm "He... Being sick is no good reason to swear. Honey, never say that word
        again."
    mc "I know I'm not supposed to, but it's so much fun to say. Fuck fuck!"
    nmc "I decided not to tell her that he was \"sick\" because of the response 
         to his swearing."
    rm "I don't have time to talk about this with the school board..."
    mc "Wait, why aren't you at work? Today is a Tuesday."
    rm ""
    return
    
    