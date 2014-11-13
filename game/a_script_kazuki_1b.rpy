label Kazuki_1d_wil:
    nmc "I walk over to Wil's desk."
    $ persistent.seen_wil = True
    $ points[3] += 2
    w "Hey, Kazuki, what's goin' on?"
    mc "Good afternoon. I suppose there hasn't been much going on, unless you wanted to count this seminar as a goings-on. What about you?"
    w "Not much, not much. Well, I'll finally have the chance to go hiking this weekend, so that will be fun."
    nmc "I looked Wil up amd down. He's actually from Colorado, taking a quarter or two of school here so he can experience the Sierra Nevada
         mountains, or something along those lines. At 6 feet, 4 inches and boasting a lean but muscle-bound frame, it's hard not to take his 
         word for it."
    $ minutes = 601
    w "Oh, and I think this woman's on some sort of crack."
    mc "That \"woman\" is at least a decade older than you are."
    w "What? No way. I thought she was a student here."
    mc "She is a student and she is here. Actually, she's working on her Ph.D now, but at some other college. She TA's here for the money."
    w "I suppose that makes sense. I still think she's bat-crap crazy. Were you here for last week's lecture?"
    mc "Yes. But I'm fairly certain that you weren't."
    $ minutes = 602
    w "Damn, you're sharp. From what I heard though, she spent 30 minutes talking about on-campus dining..."
    mc "... Even though we heard about that from the mandatory orientation..."
    w "... That a lot of people skipped..."
    mc "... Including yourself..."
    $ minutes = 603
    w "Hah... anyway, class starts soon. You should probably sit down."
    mc "Yeah, see ya... Wait, hang on. I wanted to ask you something..."
    $ cd_set(7, 7, 'Kazuki_1d_insert')
    show screen countdown
    menu:
        extend ""
        "Ask to go camping with him this weekend":
            $ answer_add("wil_camping")
            mc "Would you mind if I tagged along?"
            w "Huh? Tag what?"
            mc "I was wondering if I could go camping with you this weekend."
            w "I thought you didn't like camping."
            mc "No, It's hiking that I don't like."
            w "Well, you'd generally hike to the campsite."
            mc "Whatever. I need the exercise. Will you take me?"
            w "I don't have a reason to say no. I'll pick you up on Friday at 5:00PM, if that works for you."
            mc "We're going for a night hike?"
            w "Yeah, but I figure if you're coming along, we might as well share a meal too."
            mc "... You really don't have to do that."
            w "Actually, I do. I need feedback for a recipe I've been working on. Anyway, you'd better sit down."
            nmc "Wil wasn't exactly known for his cooking, but I'll bite."
            t "If we could all get back to our seats, we're going to dicuss how to best prepare your resumé..."
            nmc "Tamara Mirov has been the TA for this seminar as long as anyone can remember. She prefers that her \"friends\" (apparently she has
                 them) refer to her has Tammy. That's all I really know about her, and I only know that because some other TA occasionally visits
                 and calls her Tammy. I suppose I could guess that she has a good 10 years and 300 pounds on me..."
            t "... And I don't want to see any of you spacing out and pretending that you aren't here."
            nmc "I pulled my laptop out of its case and read some comics."
        "I need backup at tonight's meeting" if (answers[0] == "law_hesitation"):
            $ answer_add("wil_backup")
            mc "I'm going to need help at tonight's meeting."
            nmc "Some moral support is better than absolutely none. Besides, Wil took the accelerated Physics 101 course with me."
            w "You huh? What kind of meeting are we talking about here?"
            mc "One of those departmental bullshit ones where professors talk about nothing and somehow manage to get something done after one
                person suggests an idiotic and convoluted plan that is superior to the nothing that was previously suggested."
            w "..."
            extend "\nWhat are you, some kind of sarcastic teacher's pet?"
            mc "Something like that..."
            w "Ehh, it would probably be better if I did actual homework or something."
            mc "Whatever happened to he's before degrees?"
            w "... Okay, one, that's not how the saying goes, and two, you aren't female."
            mc "Thanks. I'll be sure to mention your name at the awards ceremony once I am formally introduced as the newest member of our city's
                 Hall of Fame."
            w "Err, we live in a town, technically."
            mc "{size=40}Go to hell!{/size}"
            nmc "With an uncharacteristic outburst of raw frustration, I return to my seat."
            w "Hey, when's the meeting anyway?"
            mc "6:00PM."
            w "Are you sure?"
            mc "I'm absolutely sure. I have an audiographic memory, remember?"
            w "... I think you just made that word up."
            mc "That doesn't make my statement false."
            w "And if you mean 'you remember everything that you hear', I don't believe you."
            mc "Considering how many more points I have than you in this class..."
            w "Whatever. Looks like Tamara is about to start her crap show."
            nmc "Nodding, I trot back to my desk."
        "Actually, never mind":
            $ answer_add("wil_nvm")
            mc "... Never mind."
            w "What?"
            mc "I... it's not important."
            w "Kaz, for God's sake..."
            mc "What?"
            w "Losing your train of thought? That ain't like you."
            mc "Ordinarily, you'd be correct, but I am feeling a bit under the weather for some reason, almost as if I didn't get any sleep."
            nmc "I awkwardly walk back to my desk, deciding not to say whatever it was I had to say."
        "...":
            call Kazuki_1d_insert
    t "All right, class is starting now... please settle down..."
    jump Kazuki_1d_tamara_b

label Kazuki_1d_insert:
    $ answer_add("wil_nvm")
    mc "..."
    w "What?"
    nmc "Realizing that I had nothing to say of significant importance, I apologize to Wil for wasting my time."
    mc "I... it's not important. Never mind."
    nmc "Sort of."
    w "Kaz, for God's sake..."
    mc "What?"
    w "Losing your traing of thought? That ain't like you."
    mc "Ordinarily, you'd be correct, but I am feeling a bit under the weather for some reason, almost as if I didn't get any sleep."
    nmc "I awkwardly walk back to my desk."
    return

label Kazuki_1d_tamara_a:
    nmc "I barely made it... again...{w} Well, technically I didn't make it, but... it's General Studies 110. No one cares."
    $ persistent.seen_tamara = True
    t "Late again, I see."
    nmc "... Except the TA herself.\n"
    extend "I consciously, yes, consciously leaned back a little. Playing on a few idioms, Tamara is 'getting too big 
         for her doorway', 'a massive woman in a small lake', 'carrying weight with the school President', but not doing a good job of 'pulling her 
         own weight'."
    call dev_com("tamaraplus")
    mc "I'm sorry, but what do you mean by \"again\"?"
    t "This is the second time you have been late to class this week. What gives?"
    $ cd_set(15, 15, 'Kazuki_1d_tamara_b1')
    show screen countdown
    menu:
        extend ""
        "She can't prove that":
            $ answer_add("tam_no_proof")
            $ points[2] += -2
            mc "I don't believe you have documentation of this first alleged tardiness."
            t "What makes you say that?"
            mc "Well, we last had this class on Thursday, and you forgot to take roll call that day."
            t "Tch... Just make sure it doesn't happen again."
        "I'll have Lawrence talk to her":
            $ answer_add("tam_lawrence")
            nmc "I don't say anything. I do however, pull out my Nokia 3310."
            t "What are you doing?"
            mc "I'm calling Professor Lawrence. I was speaking with him before I arrived here."
            t "Lawrence Henry Wright?"
            mc "That is indeed his name."
            t "That won't be necessary. I trust him. Go to your seat."
            nmc "I guess his name carries weight everywhere around here... To my seat I go, then."
        "Apologizing will get this over with faster":
            $ answer_add("tam_sorry")
            mc "My apologies, Tamara. I'll make sure it doesn't happen again."
            $ points[2] += 3
            t "Fair enough."
        "...":
            jump Kazuki_1d_tamara_b1
    jump Kazuki_1d_tamara_b
    
label Kazuki_1d_tamara_b1:
    $ answer_add("tam_indifference")
    t "... Can't get a word out, huh? Oh well, as long as the point got across..."
    nmc "Well actually, I didn't feel like gracing such a stupid question with a response, but whatever contents her."
    jump Kazuki_1d_tamara_b
    
label Kazuki_1d_tamara_b:
    $ persistent.seen_tamara = True
    nmc "Tamara Mirov has been the TA for this seminar as long as anyone can remember. She prefers that her \"friends\" (apparently she has them)
         refer to her has Tammy. That's all I really know about her, and I only know that because some other TA occasionally visits and calls her
         Tammy. I suppose I could guess that she has a good 10 years and 300 pounds on me..."
    t "All right, today we're going to discuss how to best prepare your resumé. And I don't want to see any of you spacing out and pretending
       that you aren't here. Mm-hmm, generally speaking, you start by..."
    nmc "I stare out the window and imagine myself at home doing homework. Not that I'd be doing my homework if I was home, but, whatever."
    extend " There's nothing wrong with pretending. After all, life is nothing but an act..."
    $ minutes = 610
    call triple_min(5)
    # scene bg out_the_window
    nmc "I'm not falling asleep, but I'm not giving Tamara any attention, either - my attention is directed at the traffic below."
    nmc "Traffic amuses me - not because I find cars interesting, but because of how people move about, both inside and outside of cars."
    nmc "The running man in the ridiculous Armani suit is clearly late for work. He holds an important position at his office, and whatever 
         luxury vehicle he owns is likely refused to cooperate this morning, perhaps due to leak in the coolant tank. If he had been in a 
         crash, he would have had a loaner vehicle."
    nmc "He refused the inconvenience of calling a cab, and as a result, he's taking the indignity that is the nearest bus stop. His shoes are 
         overly shiny, meaning that both the polish and shoe are cheap. At least he prepared himself for the run."
    nmc "Whether or not he has free days left doesn't matter. My guess is that his pride is either preventing him from using one for such an
         inane reason, or that there is a bonus for each unused sick day. Perhaps he works at the local AT&T office?"
    nmc "The woman at the crosswalk is likely in graduate school; she's somewhat harder to read. She is carrying both a manilla folder and a 
         laptop bag, telling me that some sort of project is due today. She isn't younger, otherwise she'd be in class, or at lunch, or at home."
    nmc "She isn't headed to work, otherwise she would be dressed a bit... differently. Her red tank top makes no attempt to cover her midriff, 
         and does a spectacular job of accentuating her relatively large breasts."
    nmc "Err, relative to other women her age, not relative to my breasts..."
    nmc "Her right arm is limp, her left arm is loosely holding the folder, and her head is down. An uncommon but not rare occurance: she was 
         depressed before leaving home. That could be due to any number of things, although a break-up would be my guess."
    nmc "Perhaps she has the mixed (in the literal sense) blessings of being both obscenely attractive and moderately intelligent, all the while
         trying to keep her priorities straight..."
    $ sio_l("bg classroom2")
    $ mlib("falarm")
    $ minutes = minutes + 5
    nmc "The blaring fire alarm snapped me out of my thought process as the sound waves crashed against my ears... why aren't flashing lights
         enough?"
    nmc "... I suppose I should be more sympathetic towards the blind."
    stop music
    nmc "I block out the alarm's sound in my mind. In all honesty, I find Tamara to be more annoying than any alarm I have come 
         across, but the alarms are generally more startling."
    nmc "... This seems to be an unwritten rule of public education systems. There is always at least one of those students. A student that craves
         attention to the point of being unable to live without it, and insists on getting it as fast as possible. And the best way to get the
         attention of an entire school has, historically speaking, been to set off an alarm, even if that alarm happens to be a church bell."
    t "Relax. It's a scheduled drill. Make your way out of the classroom in an orderly fashion..."
    nmc "... Well. I'm glad I didn't vocalize my outrage."
    extend "\nWilliam chuckles as he gets in line behind me."
    w "I know exactly what you were thinking."
    mc "Then what was I thinking, exactly?"
    w "You were thinking about how this was some silly prank some attention-hungry fool pulled off, and then you were glad that you didn't
       say so out loud."
    $ minutes = minutes + 2
    mc "Umm, no, I was exactly thinking the following: \"It seems to be an unwritten rule of public education systems. There's always at
        least one of those students..."
    w "All right, all right. I get it."
    mc "Although I'm not really sure why Tamara told us that it's a scheduled drill. The TA's aren't supposed to tell us that...\n"
    extend "I suppose Tamara has always been a bitch for enforcing rules, but not following them."
    w "Wait, is that true?"
    mc "Well, it's true that I consider Tamara to be a bitch, but I don't it would be fair to present that as a fact..."
    w "No, I mean is it true that the TA's know whether or not it's a drill, and that they aren't supposed to tell us?"
    mc "Yes."
    w "How the hell do you know?"
    mc "I own a copy of the TA's manual."
    w "... I should have known."
    nmc "I'm not one for following the rules, either. One of Lawrence's newer TAs happened to leave his manual at his desk. I took it."
    t "All right, down the stairs. Chop chop."
    $ sio_s("bg stairwell1")
    nmc "... As we walked down the stairs, it occurs to me that in a real fire, some of us would be using the elevators regardles of 
         the signs telling us not to, and that the rest of us would be in a mad dash down the stairs. Some of us would probably be 
         pushed over. Hmm... human dominoes..."
    $ minutes = minutes + 3
    "{i}Thud!{/i}"
    nmc "As if someone was reading my mind and thought \"Yes, that sounds like a good idea\", I immediately felt someone or something give me
         a strong shove."
    nmc "I quickly grabbed for the handrail with both hands, and managed to stop my fall."
    mc "Be more careful."
    nmc "I muttered a request, but I didn't bother to turn around. Both hesitation and haste cause problems, especially in heavy traffic."
    nmc "4 sets of 20 stairs later, we were outside the building and in the parking lot."
    $ sio_s("bg parkinglot1")
    w "Hoo... Why did we have to be on the sixth story...?"
    mc "You're complaining about a short trip down the stairs? Some hiker you are."
    w "One does not simply become used to walking downhill."
    mc "I suppose that makes sense."
    w "... Did the reference go straight over your head?"
    mc "Oh, no. Yadda yadda one does not simply walk into Mawdoor yadda yadda Fellowship of the Ring shut up."
    w "Mordor. It's Mordor."
    mc "Shut up anyway."
    nmc "Wil just gives me a grin, not knowing that the mispronunciation was on purpose."
    mc "You know... There is nearly no point to these drills."
    w "What makes you say that?"
    mc "In a real emergency, let's say a fire, all of the faculty would know that the alarm is not for a drill. At least one of the faculty 
        members are going to panic. One panicked faculty member.is going to startle other students, whom are going to startle other students..."
    w "What's your point?"
    $ minutes = minutes + 3
    mc "We are practicing for an un-panicked emergency when such a thing really cannot exist."
    w "... You overthink everything."
    mc "Do you think each and every student here would be well-behaved in case of, say, an earthquake? Statistically speaking, it's been
        a long time since we've had one."
    w "Fair enough. I guess we'd all be a little panicked in an earthquake. Especially if we were on the sixth story."
    mc "Do you see anyone that looks panicked at all?"
    w "Well, Lily looks a bit freaked out."
    mc "Lily?"
    w "Lilian."
    mc "Ah, yes. Lilian... Now I remember."
    $ persistent.seen_lilian = True
    nmc "Lilian is the quiet redhead in our little seminar. She always sits in the back, and even if I merely called her by name, she would, at
         best, shake once or twice, turn towards me, nod slowly, and return to whatever previously held her attention unless I said more."
    mc "Firstly, I'm fairly certain that nearly anything would make Lilian panicked. Secondly... when did you start referring to Lilian Crawford
        as 'Lily'?"
    w "I, uhh, refuse to respond to either statement. And plead the fifth. And ask for duct tape. Wait. Actually, everyone calls Lilian 'Lily'."
    mc "No, everyone calls Lilian \"Lilian\"."
    w "Well, I call Lilian \"Lily\"."
    mc "Don't tell me you've managed to fall in love with the girl. We're less than a month into the year."
    w "I can't help it. She's just my type of person."
    mc "... I was joking. Hah... At least you're honest."
    w "I try."
    $ minutes = minutes + 2
    #10:35AM
    mc "Hmm... the instructor is supposed to roll call as soon as everyone is in the designated evacuation area..."
    w "Designated evacuation area. Is that a quote?"
    mc "Yes."
    b "Oi, Kazuki. Where's Tamara?"
    mc "I don't know."
    b "You're in her class. You should know where your instructor is as long as her class is in session."
    nmc "Ben Cross is the student council president. He insists on having order, consistency and rigidity whenever possible. Especially when 
         that means being elitist or snarky. I've been trying to avoid him."
    mc "Even if that was true, I still wouldn't be legally obligated to keep track of her."
    b "Whatever. Thanks for your time."
    nmc "And with that, Ben walks away. At least he knows when to quit."
    w "... She took the elevator, didn't she?"
    mc "Yup."
    w "Oh dear."
    nmc "Being out of shape is not a valid excuse for disobeying visible placards. As far as physics and safety are concerned, an elevator shaft 
         will, to put it lightly, behave in the exact same manner as a household chimney. Those in the elevator can and will suffocate."
    nmc "The elevator however, can and should be used by firefighters to get to the various floors, both to put out fires and to rescue 
         civilians."
    nmc "... Regardless, Tamara has probably earned herself a lecture, and we won't be seeing her anytime soon."
    b "All right, evearyone is accounted for. Dismissed."
    $ minutes = minutes + 2
    nmc "Well, there's about half an hour until Math 122."
    nmc "I'm Japanese. By birth, I think I've earned the right to skip all mathematics courses until the end of time."
    nmc "Double integrals, rotations and optimizations; such topics come to me naturally."
    $ cd_set(30, 30, 'Kazuki_1e')
    show screen countdown
    menu:
        extend ""
        "Skip class":
            $ answer_add("self_skip")
            mc "There is absolutely no point in me going... but what would I do if I skipped?"
        "Attend":
            $ answer_add("self_go")
            mc "I should probably go anyway, though. Just to keep up appearances."
        "...":
            $ answer_add("self_indecisive")
            mc "... I can't make up my mind."
    jump Kazuki_1e
    
label Kazuki_1e:
    if("self_skip" not in answers and "self_go" not in answers):
        $ answer_add("self_indecisive")
        mc "... I can't make up my mind."
    li "Eh?"
    mc "Huh?"
    li "Umm, I think you were talking out loud. You seem a litle lost."
    mc "Sorry, I didn't realize. A little lost, huh? I suppose unsure would be the better word."
    li "What is there to be unsure about?"
    if("self_skip" in answers):
        mc "Well, I don't think I want to go to math today."
        $ points[3] = -1
    if("self_go" in answers):
        mc "I feel like I'm only going to math for the sake of the roll call."
        $ points[3] = -1
    if("self_indecisive" in answers):
        mc "I can't decide whether to go to math class or not."
    li "Math class... I was never particularly good at math. I'm not sure if that explains why I always skipped, or if that's because I always 
        skipped. Do you know what you would do if you didn't go to math?"
    mc "I didn't actually think about that... I think I would review some of last week's Japanese material."
    li "Kamata... that is a Japanese name. Would Japanese review actually be helpful?"
    mc "Oh. Well I was born in Japan, but my father and I moved here when I was one month old, so I didn't exactly pick up any of the language. 
        So yes, I could use the review."
    li "I see. Have you ever been to LAST?"
    mc "... LAST?"
    $ minutes = minutes + 2
    li "Yeah, Language And Science Tutors. It used to be called LASH for Language And Science Help, but apparently that sounded a little 
        naughty... {w}That was my reaction too!"
    nmc "I was about to ask what she meant by \"her reaction\", but then I realized that my forehead was resting in my right palm."
    li "Oh, I've gotta go... here's a flier, we can help... Bye."
    nmc "With that, Lilian stuffs a piece of paper in my mouth and runs back into the building."
    extend "\n... That almost didn't make sense, but then I realized that I was holding my phone in my left hand and my right hand was in my 
            laptop bag."
    nmc "I put the phone in the laptop bag and take a look at the flier."
    show asset flier last:
        xalign 0.5 yalign 0.5
    nmc "A language that sounds like J. K. Rowling's language of serpents...\n"
    extend "A science more theoretical than psychology... That was low.\n"
    extend "Last resort? Dear lord. That wasn't... amusing, albeit appreciable."
    hide asset flier last
    show asset flier last:
        xalign 0.5 yalign 0.5
        linear 1.0 yalign 7.4
    nmc "Oh wait, there's more..."
    extend "\nI see. At least they don't claim to know Parseltongue."
    hide asset flier last
    $ minutes = minutes + 3
    nmc "I unceremoniously stuff the flier in my bag. Actually, now that I think about it..."
    $ cd_set(15, 15, 'Kazuki_1g')
    show screen countdown
    menu:
        extend ""
        "Wil can get a date with Lily":
            $ answer_add("wil_lily_group")
            nmc "I'm normally not one for playing matchmaker, but I owe Wil a few favors."
        "I can get a 4.0 in Japanese":
            $ answer_add("self_40")
            nmc "To be honest, I should take advantage of this particular resource. My life is harder than I'd like it to be, and LAST sounds 
                 like it could be useful."
        "...":
            $ python_pass()
    jump Kazuki_1g
    #10:37AM

label Kazuki_1g:
    $ minutes = minutes + 3
    if("wil_lily_group" not in answers and "self_40" not in answers):
        $ answer_add("undecided_g40")
        nmc "I supposed I can decide what that means later."
    nmc "With the knowledge that there is good help available, I shove the flier in my laptop bag and head to math."
    $ sio_s("bg classroom3")
    $ minutes = minutes + 15
    mt "... Now, observe the following problem:"
    mt "... Now, observe the following problem:\n \ \ \ {size=40}∫∫{/size}{size=30}7x²+2πx+3ey²+8y+6 dA, R = (2, 8)x(1, 6.2){/size}\n{size=15}{i}\ \ \ \ \ \ \ \ \ \ 
        R{/i}{/size}{fast}"
    mt "At first glance, it seems like a daunting pile of busywork. But today, I am going to show you a surefire way to do this problem in your 
        head in less than 3 minutes."
    nmc "... I could do it in less than one minute..."
    nmc "I put my head down on my desk and..."
    mc "... {i}Snrrrk...{/i}"
    jump Kazuki_1h
    
label Kazuki_1h:
    $ ui_check = True#consider false
    $ sio_l("bg fakefog")
    window hide
    scene bg fog
    nnvlmc "..."
    nnvlmc "I fell asleep?"
    nvls "Yes. I didn't expect to see you again so soon."
    nvlmc "Where am I?"
    nvls "Well, how helpful would that information be, given that you can't leave?"
    nvlmc "Oddly enough, the fact that I can't leave tells me that I am either in Heaven, Hell, or inside of my own head."
    nvls "How perceptive. I suppose that you know which of those three would be the most likely."
    nnvlmc "Clearly, I haven't died yet... actually, for the sake of argument, I should include that theory."
    $ answer_add(nvlans(0, nvlq(None, "In front of me is an angel, this is Heaven.", "I wasn't good enough for Heaven; this is Hell.", 
        "Too good to be Hell and too bad to be Heaven; this is my head.", "There is no one else here; this is my head.")))
    nvlmc "I think I've figured it out. All right, new question..."
    nvls "I will allow you only one more question."
    nvlmc "What?"
    nvls "I said, \"I will allow you only one more question\"... although you just asked one."
    nvl clear
    nnvlmc "How childish..."
    nvls "I believe \"strict\" was the word you were truly looking for."
    nvlmc "At least tell me who you are and how you are reading my mind."
    nvls "I am a part of you. It is that simple."
    nvlmc "But... you aren't my conscience, at least not so to speak."
    nvls "That is not a fair statement. One can have multiple consciences. A conscience is {i}an{/i} inner sense."
    nvlmc "Okay, now why the fucking hell are we having this conversation in the first place... Wait. You said you didn't expect 
           to see me again so soon... Oh shit."
    nvls "That's right. You won't remember."
    nnvlmc "I received what felt like a punch to the stomach, even though the shadow did not move."
    nnvlmc "The darkness began to suck away the light from my eyes, like a funnel draining water..."
    nvl clear
    window show
    $ minutes = minutes + 12
    $ sio_l("bg classroom3")
    mt "... And Kazuki, I know you're good at maths, but this is just an insult."
    mc "Wha-what?"
    nmc "At that moment, Wil knocks his pencil off of his desk, and out of the corner of his mouth..."
    w "Goddamnit Kazuki, what the hell do you think you're doing, fallking asleep in Ms. Amniaki's class? You're in big trouble now."
    nmc "I pick myself up off of the hard surface and look around."
    nmc "The math classroom. Wil. A nondescript professor. And my classmates... they're all staring down at me, happy for some entertainment.
         They're whispering, probably insults, gossip, and laughter."
    $ mtname = "Ms. Amnaki"
    mc "Oh, so that's her name, Amnaki..."
    mt "{size=40}Get out right now! If you can't even be bothered to stay awake during my class, then I can't even be bothered to 
        see you.{/size}"
    nmc "I gather my things and make my way towards the classroom door. I know I should be feeling guilt right now, or shame. But quite 
         frankly I couldn’t care less what the teacher thinks of me now. Or my classmates for that matter, it’s not as if they don’t have 
         rumours and gossip about me already."
    nmc "However, as I'm opening the door, the teacher, seemingly frustrated by my lack of remorse, decides to add injury to the insult."
    mt "And I want a 10 page essay on my desk tomorrow about why you weren’t paying attention in class."
    nmc "I just walk out of the classroom, managing to catch a short glimpse of her beaming with pride at her ‘massive punishment’ 
         before leaving."
    nmc "And I curse her, quiet enough that no one else could hear me."
    mc "Pompous bitch."
    $ sio_l("bg parkinglot1")
    $ minutes = 830
    nmc "There is not always a good and bad, but where these opposites exist, the scale may or may not be subjective. The concept of \"good cop, 
         bad cop\", for instance, is objective. The strategy is generally defined by whatever police organization feels like employing it."
    call sn_label("sn frank")
    nmc "Cooking however, is very subjective. You could put some filet mignon in front of me and I would turn up my nose because it is not as 
         flavorful as other cuts. But put that same slab of meat in front of Frank Bruni or some other food critic, and he'll give it a few stars 
         because of how tender it is."
    nmc "The rest of math (which I spent in the hallway), and the entirety of Japanese stewed like a bad meal. And bad meals are interesting, 
         because they are bitter... but very easy to eat. After choking down the first bite, the rest chokes down easily and quickly."
    nmc "And it is, unfortunately, lunch time. Which is only bad because it is a mealtime. A wise man once said that a mealtime is just the 
         time when you shove some stuff down your throat and into your stomach because you have to."
    nmc "Fun fact, that wise man was myself."
    nmc "In any case, I have to figure out something to do for lunch."
    $ cd_set(30, 30, 'Kazuki_1i')
    show screen countdown
    menu:
        extend ""
        "I should get that essay done right now":
            $ answer_add("lunch_essay_1")
        "Don't eat and go to work early":
            $ answer_add("lunch_work_1")
        "Grab a bagel before work":
            $ answer_add("lunch_bagel_1")
        "...":
            $ answer_add("lunch_work_1")
    jump Kazuki_1i
    
label Kazuki_1i:
    if("lunch_essay_1" in answers):
        jump Kazuki_1j_essay
    if("lunch_work_1" not in answers and
        "lunch_bagel_1" not in answers):
        $ answer_add("lunch_work_1")
        nmc "... I can't actually make up my mind, so I guess I'll eat later and save myself the trouble."
        nmc "Either way, I can afford to skip a meal."
    elif("lunch_work_1" in answers):
        nmc "I don't have time to eat. I have money to make and a boss to impress."
        
    if("lunch_work_1" in answers):
        nmc "There is no rule to having exactly three mealtimes or even three meals, just that one must actually eat at some point."
        nmc "In other words, I'll work before I eat."
        #BRANCH
    else:
        nmc "I need to get to work, but before I do, I need to get another bagel because this morning's bagel turned out like crap."
        nmc "This morning's bagel was basically a circular bit of toasted bread. A real bagel needs marinara sauce, a mozzarella and 
             cheddar mix, and salami. Or perhaps cream cheese, salmon, tomatoes, and purple onions. Something besides air."
        nmc "... Salmon. Definitely salmon. And I got enough exercise this morning, so I'll go home the slow way. No shortcuts."
        
    if("law_hesitation" in answers):
        nmc "But I had better figure out whether or not I am going to that faculty thing."
        menu:
            extend ""
            "The physics department should know who I am":
                $ answer_add("meeting_known")
                nmc "If I am so important to Lawrence, then perhaps I could be of use to the entire faculty, and that relationship, 
                     of course, would be of use to me."
                nmc "That is not to say that I am selfish, but it would be good to have more influence within the school's faculty, 
                     regardless of the agenda."
                nmc "Assuming, heh, that I don't come off as a bumbling idiot."
            "Lawrence clearly needs help":
                $ answer_add("meeting_hlawrence")
                nmc "Lawrence is good enough of a professor that I should help him, plain and simple."
                nmc "I don't know exactly what's on the agenda for the meeting, but I'm sure that I'll be useful."
            "I don't have time for that":
                $ answer_add("meeting_no")
                nmc "Not only am I too busy for that meeting, but even if I did go, I'm not so sure if I'd be helpful."
    if("lunch_work_1" in answers):
        jump Kazuki_1j_skip#
    else:
        jump Kazuki_1j_lunch
        #BRANCH