# Aborted Arc + Schrödinger's Gun much? This'll be a crapload of fun.

label Kazuki_1a:#this_label_done
    #window hide
    $ ingame = "Kazuki"
    $ main_type = "kk"
    $ main_char = Combatant("Kazuki", 5, 11, 11, 20, 14, 14, 20, 100, 50, 100, 
                            100, None, 0, None, 0, None, 0, None, 0, "Fists", 
                            "Nothing", ["Pound", "Check"], "Human")
    $ main_char.setState(HP = 100, XP = 0, Belly = 65, Sleep = 75)
    $ showMCStatus = True
    $ flags = []
    $ points = init_points()
    $ reminders = []
    $ j_name = "Jonathan"
    #[needed for clocks + alert
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
    # increase this if doing something evil
    $ corruption = 0
    
    #]
    $ walletshow = True
    $ ui_check = False
    $ strchange = ""
    $ progress = "000"
    
    ###########
    
    $ shadow_name = "Shadow"
    $ s = DynamicCharacter("shadow_name", color="#808080", kind=char_black, 
        show_two_window=True)
    $ nvls = DynamicCharacter("shadow_name", color="#808080", kind=nvl_black)
    ###########
    
    $ mtname = "Math Teacher"
    $ mt = DynamicCharacter("mtname", show_two_window=True)
    
    $ dname = "\"Father\""
    $ d = DynamicCharacter("dname", show_two_window=True)

    #Rin
    $ r = Character('Rin', color="#000000", kind=char_null, 
        show_two_window=True)
    $ nvlr = Character('Rin', color="#000000", kind=nvl_null)
    
    #Lawrence
    $ l = Character('Lawrence', color='#F87431', kind=char_orange, 
        show_two_window=True)
    $ nvll = Character('Lawrence', color='#F87431', kind=nvl_orange)
    
    #Jonathan
    $ j = DynamicCharacter("j_name", color="#ADD8E6", kind=char_blue, 
        show_two_window=True)
    $ nvlj = DynamicCharacter("j_name", color="#ADD8E6", kind=nvl_blue)
    
    #Natalie
    $ n = Character('Natalie', color='#FAAFBE', kind=char_pink, 
        show_two_window=True)
    $ nvlnb = Character('Natalie', color='#FAAFBE', kind=nvl_pink)
    
    #Tamara
    $ t = Character('Tammy', color='#00FF00', kind=char_green, 
        show_two_window = True)
    $ nvlt = Character("Tammy", color='#00FF00', kind=nvl_green)
    
    #Wil
    $ w = Character('Wil', color="#FFFF00", kind=char_yellow, 
        show_two_window = True)
    $ nvlt = Character('Wil', color="#FFFF00", kind=nvl_yellow)
    
    #Ben
    $ b = Character('Ben', color="#6600CC", kind=char_purple, 
        show_two_window = True)
    $ nvlb = Character('Ben', color="#6600CC", kind=nvl_purple)

    #Lilian
    $ li = Character('Lilian', color="#00CC00", kind=char_forest, 
        show_two_window = True)
    $ nvlli = Character('Lilian', color="#00CC00", kind=nvl_forest)
    
    #Robert
    $ ro = Character('Robert', color="#FF9900", kind=char_tan, 
        show_two_window = True)
    $ nvlro = Character('Robert', color="#FF9900", kind=nvl_tan)
    
    #Athena
    $ a = Character('Athena', color="#FF0000", kind=char_red, 
        show_two_window = True)
    $ nvla = Character('Athena', color="#FF0000", kind=nvl_red)
    
    ###########
    
    #Kazuki
    $ mc = DynamicCharacter("main_name", color="#C0C0C0", kind=char_gray, 
        show_two_window=True)
    $ nvlmc = DynamicCharacter("main_name", color="#C0C0C0", kind=nvl_gray)
    
    #Internal Kazuki
    $ nmc = Character(None, what_style="main_gray")
    $ nnvlmc = Character(None, color="#C0C0C0", kind=nvl_gray_narr)
    
    ###########
    $ minutes = 460
    $ clock = True
    jump Kazuki_1b
    
label Kazuki_1b:
    scene bg blackdrop
    $ clock = False
    $ walletshow = False
    $ showMCStatus = False
    scentered "Episode 0: Understanding"
    $ clock = True
    $ walletshow = True
    $ showMCStatus = True
    $ mlib("march")
    scene bg fakefog
    with dissolve
    scene bg fog
    nnvlmc "This is my world. It is eerie, cold, and isolated."
    nnvlmc "Eerie enough that the shadows themselves are unsure of where to go."
    extend " And so cold... I can't feel myself shiver."
    extend " The isolation. I myself don't belong here."
    nnvlmc "Despite this, there is neither the feeling of pain nor the sensation
            of bliss. I merely exist, and wander through the fog. Fog so thick 
            that I could drink it..."
    extend " Pain can only last for so long. The hatred that I have felt would 
            have killed a weaker man."
    nnvlmc "...I don't understand love. I have never experienced it, and I 
            cannot recognise it."
    extend " Perhaps I had once known how to love, and love well. But those that
             I was capable of loving have since left me."
    nnvlmc "Even so, I live. For what else am I to do but join the world in its 
            cycle? The tumultuous and chaotic cycle in which there is no true 
            chain of command."
    nnvlmc "Left, and right. Left, and right. Despite my qualms, these uncovered
            feet of mine take me forwards."
    extend " Towards where, as always, is a matter of negligible significance. 
            He who wanders is he who is wayward."
    extend " My final destination, whether it be nearby or otherwise, is not 
            known to me."
    nnvlmc "Is this depression? Or simply a failure to fit in?"
    extend " This is my world, but I know neither where I will go nor where I 
            am."
    nnvlmc "I walk past an hazy image of my family. I could not see it, except 
            for in my mind."
    nnvlmc "Is that how my mother appeared when she died?"
    extend " Did my father truly once know how to smile?"
    extend " Was I truly an only child?"
    nnvlmc "My questions echo through the space around me, but I did not speak."
    nvl clear
    nnvlmc "...{w} ...{w} ..."
    nnvlmc "I knew right away... I had known... that this wasn't a dream.{w} 
            That's not to say that it felt too real to be a dream. On the 
            contrary, it felt too unreal to be a dream."
    nnvlmc "Someone else's thoughts and feelings... perhaps someone that I had 
            once known... they were overpowering my own, to the point that I 
            couldn't think or feel for myself. And there was nothing. Nothing at
            all. Nothing but a dull marching."
    nnvlmc "I am describing someone else's world. {w}This is not truly my world,
            nor the world that we humans live in. {w}Someone else is 
            controlling this place..."
    nnvlmc "Yes, a dull marching and a perfect darkness. I couldn't see, smell, 
            taste, nor touch - only hear."
    nnvlmc "I couldn't move, nor could I breathe. {w}I could do nothing but 
            merely exist.{w} Thinking itself... it could only be done in forced 
            fragments."
    $ mlib.stop()
    nnvlmc "And then the dull marching stops. I should be stressed and unsure of
            what is about to happen, but my body is relaxed."
    nnvlmc "The extraneous thoughts are cleared from my mind, but this only 
            makes me more impatient."
    nnvlmc "I knew who I was, but who am I now? And what is to become of me?"
    nvl clear
    nnvlmc "The marching... it has changed to a single pair of footsteps, and as
            if this new presence brought light with it, a dim light fills my 
            eyes, and a shallow gust flows through my lungs."
    scene bg fakefog
    show shadow norm with dissolve
    scene bg fog
    show shadow norm
    extend " And in front of me was a shadow, standing upright..."
    nvls "Stand."
    nnvlmc "My body stands up, ignoring my brain's demands to ask questions."
    nvls "See."
    nnvlmc "And now I realize that I could in fact see. I was simply unable to 
            process what I was seeing."
    nnvlmc "My body once more obeyed the shadowy voice. It belonged to an 
            equally-shadowy body. I looked into its eyes, and I saw a void. And 
            the void stared back."
    nvls "Feel pain. Remember me."
    nnvlmc "I receive what feels like a punch to the stomach, even though the 
            shadow did not move."
    call domchange("HP", -20, 1)
    extend " Pain surged through my nerves, but I did not budge nor gasp. My 
            body refused to buckle under the burning rage of the shadow, as it 
            had also been instructed to stand."
    nvls "Return."
    nnvlmc "And then the darkness covered my eyes once more, and I was returned 
            to the world of the living..."
    scene bg fakefog
    nvl clear

    $ main_name = "Kazuki"
    $ strchange = ""
    $ intchange = 1
    $ ui_check = True
    
    window show
    $ sio_l("bg kazuki bed")
    "... {w}... {w}..."
    #doublespeak l mc "What?" "What are you saying?"
    mc "Hah... hah... hah... ... huh..."
    nmc "Gasp for air. Open my eyes. Look around. Untangle myself from the 
         covers. Peel the drenched tank-top off of my body. Check my pulse. 
         Count to ten. Multiply by six."
    $ sio_s("bg kazuki bathroom")
    nmc "Walk to the bathroom. Take a deep breath. Grab the counter. Look at my
         image. One more bruise... "
    nmc "My body sluggishly obeys my brain's commands, even though I am 
         certainly wide awake. For the second time this month, my body has 
         reached panic mode before I woke up. My heart is sprinting at 180 beats
         per minute, and according to the mirror, I had just seen a phantom, 
         though they do not exist."
    nmc "I turn on the cold water, cup some of it in my right hand, and throw it
         at my face, not giving a damn about the mess I am making."
    nmc "Blink twice. Wipe my face. Breathe. Breathe again.{w}\nWhy is this 
         happening to me? What am I doing to myself? Will I get another bruise 
         tomorrow?"
    $ mlib("calarm")
    nmc "My cell phone's alarm went off, throwing my train of thought straight 
         into the mental river. Annoying. "
    $ mlib.stop()
    extend "I slide my hand towards my cell phone, turn off the alarm, and begin
            my standard morning routine, which generally consists of a
            shower, change of clothing, journal entry, breakfast, and a walk to 
            the bus stop."
    nmc "... I have wasted enough time with my little physical exam."
    nmc "So I shower. I pour the shampoo onto my head and whirl it through my 
         wet hair. My hand swipes and slams the bar of soap down my body, barely
         avoiding the new bruise on my stomach and last week's bruise on my 
         right shoulder."
    $ minutes = minutes + 2
    extend " I generally take 2-minute showers, give or take a few seconds.{w} 
            I step out of the shower and dry myself off with a black t-shirt. It
            is ripped in too many places to be socially acceptable as outdoor 
            attire."
    $ sio_s("bg kazuki bedroom")
    $ minutes = minutes + 5
    nmc "I toss the shirt on the towel rack and open my closet."
    nmc "I own 14 of everything: white tank tops, black t-shirts (excluding the 
         4 shredded ones), pairs of boxers, and pairs of athletic shorts. 
         Choosing my outfit - even on a bad day - is deciding whether I want the
         black shirt on the left side of the closet, or the black shirt on the 
         right side of the closet."
    nmc "I don't believe in fashion, and even if I did, fashion would be a 
         luxury I can't afford."
    nmc "I can afford to be efficient, though. I find it faster to haphazardly 
         hang up all of my clothing rather than fold anything."
    nmc "...I started keeping a nightmare log on my thirteenth birthday. One 
         night, I had a nightmare in which a vine coiled around me, crushed me, 
         and called my name. I asked my father if phantoms give us nightmares, 
         and he said \"not a freaking clue.\" Though, he did tell me to keep a 
         log of my nightmares, and so I bought a journal and started writing my 
         nightmares in it. Not that he ever read the journal."
    nmc "In fact, the next night, he quietly threw away everything my mother 
         left behind. She was supposed to be here, answering my questions,making
         dinner, taking me to school, not him. He thought I didn't see his 
         reluctance, he thought I didn't understand his pain, but both thoughts 
         were wrong. Who would want to nourish the reason for a spouse's death, 
         or feed a mouth that didn't work? He was a simple man, really. One that
         made sense to me."
    nmc "Regardless, I salvaged the two things that mattered: her diary and 
         wedding ring. I had opened the book to a random page: page 47."
    nmc "(June 21st, 1992)\nPhantoms, ghosts, zombies... they do not exist. All 
         that die return to the Earth, and the spirits of the dead are 
         immediately judged.\""
    nmc "According to my mother, phantoms do not exist.\n{w}I have not yet dared
         to read the other pages... this one page taught me that the writings
         of a woman can reveal precisely how disturbed she is."
    $ sio_s("bg kazuki journal")
    nmc "I go to my desk and open my nightmare log. I uncap the blue pen, and 
         scrawl out the word \"nothing\" on today's page; a carbon-copy of 
         yesterday's entry. {w}Technically, that isn't true; I remember 
         darkness, a steady beat, and a fair amount of pain. But that's about 
         it. I've been trying to figure out why I don't remember my dreams; 
         popular theories include that my dreams are boring and vague, and that 
         my brain is repressing negative memories."
    $ minutes = minutes + 5
    $ sio_s("bg kazuki bedroom")
    nmc "... Pfft. No boring dream would leave me sweaty and... bruised. The 
         latter explanation is the most likely... my phone buzzes me a second 
         time."
    nmc "I suppose that in some districts, my phone would be categorized as a 
         brick or a paperweight."
    nmc "Yes, I'm using a Nokia 3310. It does everything that I need it to do. 
         It sends and receives texts. It sends and receives calls. Best of all, 
         it wakes me up in the morning, although I do need to use an online 
         wake-up call service for that."
    mc "Crap."
    nmc "That doesn't change the fact that I have 3 minutes to get to the bus 
         stop. Grab a bagel. Grab my book bag. Bend down to put on my..."
    "{i}Crack!{/i}"
    mc "Shit."
    # scene bg ceiling
    nmc "I collapse to the floor, landing face-up. The bruise on my abdomen 
         flashes like a warhead and hurts me almost as badly. My books, laptop, 
         and bagel fall to the floor with me."
    mc "Son of a bitch."
    nmc "... Damn. No bending over for me today. That hurt enough that I should 
         probably see the doctor or something.\n{w}I can't take many more of 
         these bruises. One more and I'll be put in a body cast."
    call domchange("FP", 5, 1)
    extend " I jam the bagel in my mouth, slip on some sandals, re-gather my 
            things and rush out the door for school."
    jump Kazuki_1b_2
    
label Kazuki_1b_2:
    $ sio_l("bg city1")
    $ minutes = minutes + 5
    nmc "... I watch the bus leave the corner, taunting me with the right-turn 
         signal. My first class is 10 minutes away by bus and 5 minutes away 
         by... alternate methods."
    scene bg city1 blur
    nmc "I take a left. {w}Hop the fence surrounding the car dealership. {w}
         Hop the fence on the other side. {w}Pick the lock on the tennis courts.
         {w}Run through the courts and through D Street. {w}Jump onto Motel 6's 
         fire escape. {w}Leap into the landlord's backyard. {w}Hop the fence on
         my left. {w}Run into the school grounds."
    $ sio_s("bg classroom1")
    nmc "Push the doors to Elmer Hall open and calmly... calmly... enter room 
         307 with the rest of the students."
    nmc "... God dammit, my abs still really hurt. Adrenaline is one helluva 
         drug, I suppose."
    $ minutes = 485
    nmc "As I breathe in the stale classroom air in an attempt to catch my 
         breath, the bruise reawakens from its nap."
    mc "Haah... hoo... ow... shit..."
    nmc "My classmates turn towards me..."
    j "Shit-told you to never talk to her again, huh? Rough love life, you got 
       there."
    nmc "I force a frown in order to go with Jonathan's save. Besides, his save,
         for the most part, was very true."
    mc "Yeah... pretty much."
    j "Better luck next time, eh?"
    nmc "Jonathan is the closest thing I have to a best friend. We met two years
         ago, when he moved here from who-knows-where; he never told me. To make
         a long story short, I helped him study, his mother's maidservant 
         provided meals, and we eventually bonded as we discovered how similar 
         we really were. For instance, neither of us had a girlfriend at the 
         time, nor did either of us speak to our mothers. We agreed to ignore 
         the fact that my mother is dead."
    nmc "I take my seat next to Jonathan and watch the rest of the class settle 
         down. The door opens again, but this time, the man entering the room 
         locks the door.\n"
    extend "Professor Lawrence, the Physics 102 teacher, locks the door at 8:05 
            AM sharp. And attendance matters in his class."
    nmc "\"If you're late for a morning class, then you're either paying for my 
         coffee, or paying for your test. If you're late for an afternoon class 
         well, then you're just stupid.\""
    nmc "According to an urban legend, a student was late for a single 8:05 AM 
         class, and received a 0 on the upcoming midterm. Another student was 
         late for a 3:15 PM class, and had the option to wear a dunce cap rather
         than take the 0."
    nmc "... I'm still not sure a dunce cap would be an effective punishment. 
         That aside, I like Professor Lawrence. He refuses to put up with 
         nonsense, he maintains formality, and he gives me high marks."
    l "Today I'm going to review Gauss's law and electric potential, since they 
       have been the topics of my office hour discussions for the past four 
       days... I probably should have done that earlier, but you clowns never 
       speak up unless you're with me alone... And the next time you laugh at 
       something I say, be prepared to explain the humor to the entire class..."
    nmc "Topics I already know. I tune Professor Lawrence out, open irssi on my 
         laptop and enter:"
    "/server 69.42.124.63\n{w}/join #physjabber ew1hf1QW!d\n{w}/nick kazokaz\n
     {w}/msg nickserv identify ewR@!fj12rocketbananaboat"
    nmc "I stretch my fingers and begin talking with my classmates."
    #]
    
    #the if statement is a relic of a bugfix, leaving it here for now
    if(True):
        nvln "{color=#C0C0C0}%%kazokaz{/color}: Good morning, Jonathan.{fast}"
        extend "\n{color=#ADD8E6}+jonrod{/color}: still can't believe you swore 
                in class lol{fast}"
        extend "\n{color=#C0C0C0}%%kazokaz{/color}: Shut up.{fast}"
        extend "\n{color=#FFFF00}willard92{/color}: you guys are so productive 
                in the morning{fast}"
        extend "\n{color=#FFFF00}willard92{/color}: best use of a physics 
                lecture ever{fast}"
        extend "\n{color=#C0C0C0}%%kazokaz{/color}: Then I can assume you are 
                making excellent headway on your English essay?{fast}"
        extend "\n{color=#FFFF00}willard92{/color}: yes{fast}"
        extend "\n{color=#ADD8E6}+jonrod{/color}: bullshit{fast}"
        extend "\n{color=#C0C0C0}%%kazokaz{/color}: Technically, now you're 
                swearing in class...{fast}"
        extend "\n{color=#ADD8E6}+jonrod{/color}: lolno{fast}"
        nvl clear
    $ minutes = 515
    nmc "Never mind. IRC is a waste of time. I pull out my notepad and focus on 
         the lecture."
    #]
    
    #[scene4
    "... "
    $ minutes = minutes + 25
    extend "... "
    $ minutes = minutes + 25
    extend "..."
    $ minutes = 585
    l "... And that concludes today's lecture. There will be a quiz on Gauss's 
       law and electric potential next week..."
    nmc "But the second sentence fails to reach the now-absent ears. The 
         students stampede out of the room, not caring about how the columns of 
         desks transform into a scattergram. I watch several desks even make 
         their way out of the room and into the hall."
    extend "\n... I don't follow them. Instead, I stay to speak with Professor 
            Lawrence."
    l "... Rutabagas. "
    mc "I beg your pardon?"
    l "Oh, hello Kazuki. I use the names of generally unpalatable vegetables in 
       the place of traditional curse words... and I think my reason
       for cursing itself is obvious."
    mc "First, with all due respect, I find rutabagas to be delicious, 
        especially when fried under a layer of ground garlic with grapeseed oil.
        Second, wouldn't it be more appropriate for you to use the names of 
        obscure physicists? For instance, \"Oh for Merkel's sake\" instead
        of \"Oh for Pete's sake\"?"
    l "... Angela Merkel is a physicist?"
    mc "Precisely my point."
    l "Interesting. Well, you must have had something intelligent to say or ask 
       since you didn't stampede out with the rest of them. Am I right?"
    mc "Uhh..."
    nmc "I end up asking about..."
    $ cd_set(7, 7, 'Kazuki_1b_pre')
    #$ override_mouse_set(600, 420, "fake_1", "surprise")
    show screen countdown
    menu:
        extend ""
        "Today's lecture":
            #$ activate_mouse_hack()
            $ add_answer("law_lecture")
        "The upcoming test":
            $ add_answer("law_test")
        "Nothing at all":
            $ add_answer("law_nothing")
        "...":
            $ add_answer("law_hesitation")
    jump Kazuki_1b_pre
    #call domchange("HP", -1, 1)
    #!URGENT : WRITE HERE!#

    
label Kazuki_1b_pre:
    if ("law_lecture" in answers):
        mc "There were a few concepts in today's lecture I didn't quite understand."
        l "Liar. I know you understood everything."
        nmc "Perceptive as always..."
        mc "God. I was just making conversation."
        nmc "Lawrence lets out a little chuckle."
        l "I'm kidding. Run along now."
        nmc "I didn't have anything else to talk about, so I left the room."
        mc "See you on Monday."
        l "Ciao."
        $ points[0] += 1
        #9:45PM
    elif ("law_test" in answers):
        mc "I was hoping I could ask you a few questions regarding the upcoming 
            test."
        l "Well, I won't be answering any."
        mc "Okay... I meant that I fully understand Gauss's law, but I am having a 
            hard time memorizing it."
        l "Oh. That's easy. Rather than memorize what goes where, just remember the 
           letters."
        mc "What?"
        l "{size=30}Φ{/size}{size=14}E{/size}{size=30} = Q/{/size}
           {size=40}ϵ{/size}{size=14}0{/size}"
        mc "... What?"
        l "Phi-sub-E is equal to Q divided by epsilon-sub-theta."
        mc "Oh. Thanks. That's a lot easier than the electric flux through some 
            isolated surface is equal to the total charge within... whatever."
        nmc "To be honest, I was acting, and I think Lawrence saw through it, but 
             played along anyway for the sake of using it as a conversation
             starter..."
        nmc "... However, said conversation goes on for another 15 minutes, with
             Lawrence giving a one-on-one lecture on Greek history (among other 
             things), and me not giving a damn about the time waste."
        call triple_min(5)
        l "... which is why Mr. Lehrer would end with \"There's earth and air and 
           fire and water.\" You really should give it a listen sometime."
        mc "Perhaps I will... I honestly prefer his less scientific work."
        l "Don't actually go poisoning pidgeons in the park though... oh, Noether 
           dammit. You have to get going."
        nmc "... It's 10:00AM... My next class is in 5 minutes..."
        mc "Crap! I'll see you later!"
        nmc "Lawrence lets out a burst of hearty laughter as I knock over yet 
             another desk on my way out."
        l "I wonder if anyone has actually had the gall to name their child 
           'Crap'... That would make a great last name..."
        $ add_answer("nat_xc-skipped")
        $ points[0] += 3
        #10:00PM
        call triple_min(2)
        jump Kazuki_1c
        #skip Kazuki_1b_extend
    elif ("law_nothing" in answers):
        $ answers.remove("law_nothing")
        $ add_answer("law_hesitation")
        mc "Actually, there was nothing I wanted to ask..."
        l "Oh. Well then. Get. Out."
        $ points[0] += -2
        nmc "He starts waving me towards the door, but..."
        l "Oh actually, I do have something to ask of you."
        call Kazuki_1b_stub
    else:
        $ add_answer("law_hesitation")
        mc "... Uh..."
        nmc "I am always prepared to make conversation. I am rarely prepared to 
             begin a completely new one.{w} ... Fortunately, Professor Lawrence 
             interjects before I have to pretend to be interested in some useless 
             trinket."
        l "Well, if you have nothing to say, I actually do have something."
        call Kazuki_1b_stub
    jump Kazuki_1b_extend
        
label Kazuki_1b_stub:
    mc "Do tell."
    l "Tonight, there will be a faculty meeting for the undergraduate division 
       of the physics department. Needless to say, I'll be there."
    mc "... And you'd like me to join you? I can't see how my presence would be 
        conducive to your purpose."
    l "You'll have to speak up. I didn't catch that last bit."
    nmc "I think that's another way of saying 'I have no damn clue what that 
         c-word means'."
    mc "I don't know what good I'd do. We're only 3 weeks into this quarter, and
        this is my first year at this school."
    l "That's not true at all. We were going to discuss restructuring the way 
       physics is taught during Summer Session II."
    nmc "Oh yes. Let's have me sit around with a score of elderly strangers so 
         that I can enlighten the department on the 341 faults I found in the 
         accelerated teaching of Physics 101. Not only would that be a 
         well-received service, but my time could not possibly be used 
         on a more worthwhile task."
    $ minutes = minutes + 3
    l "It's at 6 o'clock tonight, and will probably end at 7:30. If it matters, 
       complimentary dinner will be catered from..."
    $ reminders.append("meeting at 6:00PM")
    nmc "Sold. I can set aside 90 minutes to earn a meal."
    l "... from what I understand, you normally attend cross-country practice at
       that time, or am I mistaken?"
    mc "No, I do normally have cross-country at 6:00PM on Tuesdays."
    l "Today, you don't. I had your practice moved to 8:00PM."
    mc "... You did what?"
    l "Coach Cyrus and I are on very good terms. I told him I absolutely needed 
       the field for my model rocket experiments."
    mc "... You must be joking."
    l "Physicists are the best commedians. I actually am testing out a new 
       chemical formula for fuel. I'll probably manage the tests remotely 
       with my phone until the meeting actually starts."
    nmc "It occurs to me that Lawrence really is the type of person who would 
         build a few rockets and formulate a new few recipe just to get one of 
         his students out of something."
    l "So, are you coming?"
    $ minutes = minutes + 2
    #9:50PM
    $ cd_set(20, 20, 'Kazuki_1b_interstitial')
    show screen countdown
    menu:
        extend ""
        "Yes":
            mc "I should be able to attend. Should I just come to this classroom at 6 
                then?"
            l "Yes. You won't be able to get into the meeting without my key. I'm 
               counting on you."
        "No":
            mc "I don't think so."
            l "Well, meet me in this classroom at 6 if you change your mind."
        "...":
            l "Not sure, eh? Well, if you do decide to come, meet me in this 
               classroom at 6. Ciao."
    return
    # ^ jump Kazuki_1b_extend
        
label Kazuki_1b_interstitial:
    l "Not sure, eh? Well, if you do decide to come, meet me in this classroom at 6.
       Ciao."
    return
        
label Kazuki_1b_extend:
    nmc "And with that, he ushers me out of the door."
    $ sio_s("bg hallway1")
    mc "Ah, dammit..."
    nmc "I visualize today's schedule in my head."
    if ("law_hesitation" in answers):
        nnvlmc "8:05AM - 9:45AM: Physics 102\n{w}
                10:05AM - 11:00AM: General Studies 110\n{w}
                11:05AM - 12:00AM: Math 122\n{w}
                12:05PM - 1:45PM: Japanese 101\n{w}
                2:00PM - 5:50PM: (Work + lunch)\n{w}
                6:00PM - 7:30PM: (Stupid faculty thing)\n{w}
                8:00PM - 10:00PM: (Cross-country practice)"
    else:
        nnvlmc "8:05AM - 9:45AM: Physics 102\n{w}
                10:05AM - 11:00AM: General Studies 110\n{w}
                11:05AM - 12:00AM: Math 122\n{w}
                12:05PM - 1:45PM: Japanese 101\n{w}
                2:00PM - 5:50PM: (Work + lunch)\n{w}
                6:00PM - 8:00PM: (Cross-country practice)"
    nvl clear
    nmc "I hate Tuesdays. And Wednesdays. Well, I don't hate the days 
         themselves, but the manner in which my classes are scheduled for those 
         days. I like my classes for the most part, but 6 hours of non-stop 
         education? Ridiculous. It's such a shame tha-"
    $ persistent.seen_natalie = True
    n "Hey..."
    nmc "... I cannot believe I didn't notice that Natalie Bellangerd was 
         standing there. She can have my train of thought whenever she wants it. 
         Cute face. High placement scores. Co-captain of the cross-country team.
         And such a great body..."
    extend "\nWhy is she talking to me?"
    mc "H-h... hey Natalie..."
    nmc "My words whistle as they leave my mouth. I take the opportunity to 
         clear my throat."
    n "You're Kazuki, right?"
    nmc "Oh my God. She knows my name."
    mc "That's me. What's up?"
    n "Are you going to cross-country today?"
    $ cd_set(5, 5, 'Kazuki_1b_fail')
    show screen countdown
    menu:
        extend ""
        "Yes":
            #technically a second logic block
            mc "Yes, why do you ask?"
            n "Well, I was hoping you'd be able to take me to cross-country practice."
            nmc "Oh God. She wants me to do her a favor. Wait, that can't be right.{w} I
                take the opportunity to clear my throat again and calm down."
            mc "Can't your boyfriend do that?"
            n "You say that as if I have a boyfriend."
            mc "... You're single? None of the guys here are good enough for you?"
            n "I would be a bad judge of that. Perhaps you don't listen to gossip, but 
               I'm a lesbian."
            nmc "... That was embarassing. Now I know I'd never have a chance with her. 
                 Time to walk away... wait. Something is still wrong."
            mc "Don't you normally walk to cross-country practice?"
            n "I don't want to do that at 8PM... Just because I'm lesbian doesn't mean 
               that I'm not a girl. I'm probably easy to pick on."
            nmc "Natalie gives me a surprisingly pronounced frown."
            $ minutes = minutes + 2
            if ("law_hesitation" in answers):
                mc "I suppose the school could get a bit dangerous at this time of the 
                    day. You knew Prof- err, Coach Cyrus had the practice moved?"
                n "Yeah, he sent out an email late last night."
            else:
                mc "I suppose the school could get a bit dangerous at this time of the 
                   day. Wait. 8PM?"
                n "Yeah, Coach Cyrus had the practice moved. He sent out emails and 
                   texts late last night."
            nmc "Natalie lets out a yawn. So cute."
            mc "Did he...?"
            nmc "I pull out my phone. The e-mail was sent at..."
            mc "... 3AM this morning?"
            n "Mmm. I think I need a nap."
            mc "What the hell were you doing at 3AM in the morning?"
            $ sn_draw("sn gre")
            n "Studying for the GRE's..."
            mc "Already? I thought you were a junior."
            n "No... I'm a senior. Ideally, I'll get into a good graduate school that 
               lets me both run and study medicine, but I'll have to take what I can 
               get."
            mc "Oops. My mistake."
            $ minutes = minutes + 3
            nmc "I am just noticing that I'm having an easier time talking to her, now 
                 that the shock of her starting the conversation has passed."
            n "No worries! I get the whole \"you look young\" thing a lot. So I'll take 
               that as a compliment."
            nmc "She sticks her tongue out, despite her red and baggy eyes. I start to 
                 force a laugh, but I stop myself as I see her start to speak again."
            n "Well, I should probably get to my next class. So, will you be able to- 
               eep!"
            nmc "Her legs buckle and she starts to fall! I..."
            $ cd_set(4, 4, 'Kazuki_1b_extend2')
            show screen countdown
            menu:
                extend ""
                "Catch her!":
                    pass
                "...":
                    pass
            jump Kazuki_1b_extend2
        "No":
            $ add_answer("nat_no_or_hesitation")
            mc "No, why do you ask?"
            n "Well, I was hoping you'd be able to take me to cross-country practice, 
               but if you're busy..."
            nmc "My throat collapses in on itself. God, I should have said yes. And now 
                 I physically can't change my mind."
            n "S... sorry for bothering you!"
            nmc "My throat remains closed. I let out something like a wheeze as wisps of
                 air rattle off of my dry throat. Natalie walks off."
            mc "Dammit."
            $ points[1] += -2
        "...":
            $ add_answer("nat_no_or_hesitation")
            nmc "I can't say anything in front of the perfect Natalie. What if I
                 stutter? What if I spit on her? What if I..."
            n "Oh... Umm, s-s-..."
            nmc "... Better not to say anything at all."
            n "Sorry for bothering you!"
            nmc "And with that, she runs off. Even with a textbook in one hand, she
                 still runs faster than I do. By quite a bit."
            mc "Hah... as expected of the great co-captain of the cross country team..." 
            $ points[1] += -2
    jump Kazuki_1c
    
label Kazuki_1b_extend2:
    nnvlmc "... Natalie never hit the floor."
    nnvlmc "It took me a full 5 seconds to realize that Natalie was in my arms."
    nnvlmc "... My body didn't even wait for me to make a decision. It moved all
            on its own, and embraced her. "
    extend "\nIt took another 5 seconds to realize that her soft chest was 
             pushed into mine. "
    extend " Her eyes are closed and her head is down. Her long platinum hair 
            makes a veil blocking my view of her face. "
    nnvlmc "The blissful sensation of her willowy frame being held up by my own 
            hands."
    nvl clear
    nmc "... Natalie breaks the silence before I can."
    n "Hehe... thanks. I'm normally not this clumsy."
    mc "You really shouldn't go to bed that late."
    nmc "That's when I realize... she is still in my arms. And that I am still 
         in hers."
    extend "\n... I let go of her. Reluctantly. But quickly."
    n " So umm... will you be able to walk me over at a quarter to 8?"
    $ cd_set(5, 5, 'Kazuki_1b_fail')
    show screen countdown
    menu:
        extend ""
        "Yes":
            $ add_answer("nat_will_try")
            mc "Yeah, I'll come get you."
            n "Oh, you're the best. Here's my address."
            nmc "She neatly scrawls - yes, neatly scrawls - her address on a notecard 
                 and hands it to me."
            mc "Wait, you can't drive there?"
            n "Well... I don't quite have my driver license yet."
            mc "Seriously?"
            n "So both of my parents work until 8:00PM every day, but the DMV closes at 
               4:00PM. That means that I can't take the driver's test unless someone 
               drives me. And with gas and time being as valuable as they are, that 
               doesn't happen very often. And the one time someone gave me a ride to the
               DMV, two kids ran through the diagonal of the intersection during the 
               test..."
            nmc "Only Natalie would be cute while making tens of excuses. There is a bit
                 of irony to Natalie being able to do nearly everything except for the 
                 simple act of driving."
            extend "\n...{w} ... "
            extend "She's still going..."
            n "... apparently, when that happens, you're supposed to come to a 
               complete stop rather than swerving, even if you can't come to a 
               complete stop safely, since..."
            $ minutes = minutes + 1
            nmc "I could listen to her all day, but I should really get to class..."
            n "... Well, thanks for listening! I need to get to my next class. See 
               ya later!"
            nmc "Perfect. So do I."
            mc "Later!"
            nmc "..."
            extend "\nI wonder if she fell on purpose."
        "No":
            $ add_answer("nat_no_or_hesitation")
            nmc "I sadly shake my head. I'm a very busy man, with things to see and
                 people to do. Or something along those lines."
            $ points[1] += -2
            mc "Sorry, but I have to be somewhere."
            nmc "I walk off towards my next class, not looking back..."
        "...":
            jump Kazuki_1b_fail
    jump Kazuki_1c
    
label Kazuki_1b_fail:
    nmc "I can't say anything in front of the perfect Natalie. What if I 
         stutter? What if I spit on her? What if I..."
    n "Oh... Umm, s-s-..."
    nmc "... Better not to say anything at all."
    n "Sorry for bothering you!"
    nmc "And with that, she runs off. Even with a textbook in one hand, she 
         still runs faster than I do. By quite a bit."
    mc "Hah... as expected of the great co-captain of the cross country team..." 
    nmc "I accept my 402nd failure at speaking to a female, and head to my next 
         class..."
    $ add_answer("nat_no_or_hesitation")
    $ points[1] += -2
    jump Kazuki_1c
    
label Kazuki_1c:
    $ jump_break()
    jump Kazuki_1c_continue
    
label Kazuki_1c_continue:
    #WRITEHERE#...
    $ sio_l("bg classroom2")
    if ("law_test" in answers):
        $ minutes = 606
        jump Kazuki_1d_tamara_a
    else:
        $ minutes = 600
        nmc "Well, I still have 5 minutes before class actually starts. I should
             probably..."
        extend "\nHeh. Class. I look around the \"classroom\". The \"teacher\" is 
                organizing unimportant papers on her desk."
        nmc "That's the problem with these seminars. Some unexperienced girl only a  
             few years older than myself is trying to give advice to her similarly 
             unexperienced peers, and with regards to how to live."
        extend "\nOne wonders how these blasted community colleges are still 
                standing. Oh right, they're obscenely cheap."
        nmc "I wonder how much those seminar interns get paid. Probably too much."
        $ minutes = 601
        nmc "Well, I have 4 minutes left to kill. I should probably have a chat with
             Wil. To be honest, I don't really care how he decides to use his time 
             before class, but since he is technically a friend of mine, it would 
             only be just to offer the same concerns that he has offered to me."
        jump Kazuki_1d_wil