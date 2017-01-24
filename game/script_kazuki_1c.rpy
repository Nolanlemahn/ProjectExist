label Kazuki_1j_skip:#we skipped lunch
    $ sio_l("bg workshop")
    $ minutes = minutes + 5
    #1:55PM
    call impossible_problem_1
    $ minutes += 30
    #2:25M
    nmc "Robert Hale has been the proud owner of Robert and Son's Machines for 
         as long as anyone can remember, which is of course, not very 
         long at all. This in itself is a bit awkward, since Robert lost custody
         of his son when he was divorced. But changing the name of his little 
         shop would be an expensive pain in the ass in terms of both paperwork 
         and physically changing the sign, so the name stuck."
    extend "\nHis words, not mine. There have been a few awkward moments though,
            when I have been mistaken as his son..."
    nmc "In any case, I happen to work for him. Three hours a day, by the sweat 
         and grime of my brow, wrench in hand... actually I just handle the 
         taxes, the telephone, and the computers."
    mc "Hello, Robert and Son's Machines. Yes, we can service your BMW. Yes, I 
        can schedule you for Monday. Certainly. Good day to you too."
    $ minutes = minutes + 15
    $ sio_l("bg workshop")
    mc "Yes, Robert and Son's. No, we don't take walk-ins. No, the manager is 
        actually working on a car at the moment. '99 Ford Explorer actually, 
        but... No, we are completely booked for Friday... We don't actually work
        on Saturday. Next Tuesday will work. Of course. Enjoy the rest of your 
        afternoon."
    $ minutes = minutes + 15
    $ sio_l("bg workshop")
    mc "Hello, Robert and Son's Machines... I see. Fuck you too."
    nmc "Now normally, that sort of language would get me fired and could get me
         sued. However..."
    ro "Kazuki, was that Rachel on the phone?"
    mc "Yes sir."
    ro "What a bitch. Carry on."
    nmc "Rachel made the mistake of trying to get her cell phone repaired here. 
         Not that we couldn't have repaired it, but she insisted that we repair 
         the phone for free and deliver the repaired phone on the same day the 
         phone was brought in."
    nmc "A ridiculous customer by all accounts. So basically, everyone in the 
         office hates this customer more than any other."
    ro "Oh, how's tomorrow's schedule looking?"
    mc "Completely booked."
    ro "And Monday's schedule?"
    call sn_draw("sn siebener")
    mc "One car. A Siebener. Nothing else for Monday."
    ro "I hate working on beemers. Tuesday?"
    mc "No cars at all. The whole week is basically empty, actually. I might not
        be needed for most of the week. Although I could still come in if you'd 
        like. Here, look at the schedule."
    nmc "There are indeed schedules worse than an overbooked one. Because even 
         if you are working overtime, you are still in fact working, and 
         therefore being paid. When we have an underbooked schedule, we spend a 
         lot of time twiddling our thumbs and since our salaries are 
         comission-based, we also don't get paid as much."
    ro "I didn't think it would be possible to have less business this week than
        last week. I'll have someone else do the phones on Tuesday. Take Tuesday
        off."
    mc "To be fair, I haven't scheduled any appointments yet."
    ro "True."
    mc "Also... You could show me how to repair something instead."
    ro "Nope. You aren't licensed for... anything. Even if I did show you the 
       insides of an iPhone, it would be all kinds of illegal for you to do paid
       work. Unless you want to fix another coffee maker."
    mc "... I suppose I learned my lesson with the first coffee maker."
    nmc "Robert was of course, referring to \"The Ground Problem\", or at least,
         that's what he calls it when he retells the story to customers. Ground 
         floor, ground coffee, haha."
    nmc "Although Robert is technically a mechanic, a few customers began to 
         bring their computers to us. Originally, we told them that we didn't 
         have any computer parts. One Tuesday however, I told Robert to let me 
         take a look at it, and as it turned out, the problem was between the 
         desk and the chair."
    nmc "\"My computer won't connect to the Internet!\" The problem wasn't the 
         network interface controller, which is, of course, the thing that the 
         silly-looking blue wire goes in. The problem was actually with the 
         settings on the operating system. Somehow, the computer was trying to 
         use Google as a router. I was honestly impressed."
    nmc "... That's kind of like trying to use beef to fertilize the grass that 
         cows eat. Which only makes sense if you know nothing about 
         farming. Ignoring the fact that some farmers do directly feed their 
         livestock animal by-products. Which is basically bad beef."
    nmc "Anyway, I fixed the computer. The next day, I was admittedly cocky and 
         tried to fix a coffee machine without telling Robert."
    nmc "Long story short, the carpet has a very large coffee stain in it."
    ro "Well, there are no cars left to work on, so I'm taking a nap."
    mc "Understood."
    nmc "And so, I allow another monotonous day of appointment scheduling and 
         paperwork to drag on."
    $ sio_l("bg blackdrop")
    $ triple_min(25)
    $ sio_l("bg workshop")
    #3:55PM
    nmc "I had run out of tasks for today, so I began to record data of the cars
         Robert had worked on over the past week."
    nmc "Specifically, the more useless data. Such as, that 60.3 percent of the 
         cars that came through our shop were originally painted white."
    nmc "Or that 32.4 percent had failed their previous smog check."
    nmc "Considering that I'm really not in the mood to work on my essay, this 
         seemed to be a reasonably good use of time."
    nmc "I lost myself in the spreadsheets in Robert's computer..."
    jump Kazuki_1l_work
    
label Kazuki_1j_lunch:#originally had a bus crash intended; bad idea
    # 1:50PM
    $ minutes = 830
    $ sio_l("bg bus1")
    nmc "As I confirmed this morning, it takes 5 minutes to get to school if I 
         sprint, trespass, pick a few locks, jump dangerously, and so on."
    nmc "But honestly, I'm not up for repeating all of that nonsense. So, I'm 
         taking the bus home."
    $ sio_l("bg blackdrop")
    call triple_min(2)
    nmc "The rest of the bus drive proceeded without incident."
    $ sio_l("bg kazuki kitchen")
    nmc "I let myself into the apartment and begin getting things out of the 
         refrigerator."
    nmc "Father doesn't own a car. He had a Subaru, but then he sold it to pay 
         off his tab. So I can't actually tell if he's home or not."
    nmc "Not that I care."
    mc "...Freaking why."
    nmc "While all of my smoked salmon was where I left it, someone had eaten 
         the last bagel after I left for school."
    nmc "I suppose white bread will have to do."
    "{i}Clatter!{/i}"
    mc "Who's there?"
    nmc "Without double-checking whether or not someone has actually joined me 
         in the room, I get ready for a skirmish."
    nmc "I snap my wrist and adjust my grip of the butter knife, holding it as I
         would a dagger. It may not be particularly sharp, but it is threatening
         enough."
    nmc "The sound had been loud and unexpected, but its source is..."
    d "Go back to school, you little faggot."
    nmc "Father either just got back from the bar, or has just woken up with a 
         hangover. Either way, he is hostile."
    nmc "In his drunken swagger, Father had succeeded in knocking my plate to 
         the floor. Although gaudy, these new plastic plates are proving to be 
         nigh-unbreakable, saving me several dollars a day on housekeeping."
    mc "Tsk..."
    nmc "... He swings at me with his left arm, but I drop to the ground. The 
         fist connects with nothing but air. I have a free shot here.{w} I push 
         hard with my right elbow, crushing his diaphragm. He falls over, 
         wheezing."
    nmc "It takes considerable self-control to not use the knife."
    mc "You'd be in jail and out of alcohol if I wasn't paying for this place, 
        dumbfuck."
    nmc "I put down the knife, and twist a rubber band around a bundle of 5's 
         from my wallet. Father's beer money for the week."
    $ main_char_cash -= 50
    mc "And I'm going to work, not school. Once I shove some bread and meat down
        my throat, anyway. Which reminds me. Stop eating my crap. I need my 
        bagels."
    nmc "In response, Father gets up and takes another swing at me. Persistent 
         bastard."
    nmc "I slam a cutting board into his head, hopefully putting him down for a
         bit longer than a few seconds. The board shatters into pieces around
         us."
    d "Hnngggrr eaaaaah-"
    nmc "Father collapses to the floor, making a gargling sound. I drop the
         remains of the cutting board into the trash - the glass shards are 
         no longer useful for kitchen use."
    nmc "... We needed to get a plastic one, anyway."
    mc "You haven't won a fight since I turned 14... I'm leaving now."
    nmc "Father, still on the floor, lifts his right hand and makes a \"blah 
         blah\" motion with it. An unsuspecting target for the wad of cash. The 
         money drops to the floor with a light rustle. I can't resist a smirk as
         I lift the plastic plate off of the floor while he picks himself up."
    d "I wasn't ready."
    mc "You were always shit at catch."
    nmc "He bends over to pick up the money, and his back makes a cracking 
         sound. My \"bagel\" made, I make my way towards the door."
    d "Kill me, goddammit. Put me out of my misery. I know you want to."
    nmc "I stop walking, but I don't look back."
    mc "As much as it disgusts me, you were the last thing my mother ever 
        touched. If it wasn't for that, you'd have three bullets through your 
        skull."
    nmc "I open the door and head out for work, intentionally leaving it open."
    jump Kazuki_1k_work

label Kazuki_1j_essay:
    nmc "... A 10 page essay on why I wasn't paying attention in class."
    nmc "\"Well gee, Ms. Amnaki, it may or may not have to do with your 
         inability to teach things that are new to me.\""
    nmc "Mmm, an excellent topic sentence."
    nmc "\"Additionally, due to the nature of your teaching style, all I need to
         do is briefly scan the 40' x 30' whiteboard to gain a full 
         understanding of the day's lesson. For instance, on the day that you 
         gave me this assignment, you were in the middle of a simple 
         two-dimensional rotation problem...\""
    nmc "... I can absolutely get the rest of this essay done in 10 minutes. 
         Right? As long as I get to work by 2:30 or so, everything will be 
         fine..."
    $ minutes = minutes + 2
    $ sio_l("bg library1")
    nmc "And you were showing us how to transform matrices in a manner that... 
         oh."
    nmc "... I'm not actually getting anything done..."
    $ essay_status = "a skeleton"
    nmc "I'm saying and typing a lot, but none of it is truly essay material."
    $ triple_min(10)
    nmc "\"In short, because your online notes are far clearer than you are 
         while lecturing, there is no real reason to pay attention in class.\""
    mc "... That's no good either."
    li "And now you seem angry."
    nmc "An unexpected but famiiliar voice rings through my eardrums, kindly 
         pointing out that I am visibly losing control of my emotions."
    mc "... How long have you been standing there?"
    li "Mmm. I dunno."
    mc "Well, when did you get here?"
    li "Don't know that either!"
    mc "Insufferable little..."
    nmc "I mumble the rest of my statement. Lilian sticks her tongue out, and 
         folds her hands behind her back."
    li "I heard that!"
    $ minutes = minutes + 5#2:27
    mc "I don't believe you."
    nmc "Lilian puts her tongue back in her mouth and frowns."
    li "You called me a bitch."
    mc "Dammit."
    li "Really, though. Whatcha working on?"
    nmc "Happily inviting herself to my table, she jumps into the seat on my 
         right."
    mc "I didn't say you could set next to me."
    li "Ah, but that's not important right now."
    nmc "I sigh, and tell Lilian how I fell asleep in today's math class and as 
         punishment, have to write a paper."
    li "Oh. On why you fell asleep?"
    mc "Yes, unfortunately. I don't know how anyone could write 10 pages on the 
        subject."
    li "Hee! You could write \"I am a moron.\" over and over again!"
    mc "... Even if I was willing to deprecate myself in that way, I don't think
        Amnaki would accept that. "
    extend "Although, using the same sentence repeatedly... eh, that sounds like
            the amount of effort I'm willing to put into this stupid 
            assignment."
    li "I figured as such. Would you like some help?"
    mc "Err... why are you offering?"
    li "So I can remind you that joining LAST is a good idea!"
    mc "That figures."
    li "Wah! I'm not actually that self-centered. That was a joke."
    mc "Ugh. You aren't a funny person."
    li "Okay really, I just don't have anything better to do. Do you want help 
        or not?"
    $ cd_set(15, 15, 'Kazuki_1j_essay_what')
    show screen countdown
    menu:
        extend ""
        "Yes":
            $ addAnswer("lily_essay_1_yes")
            call Kazuki_1j_essay_yes #returns
            if("self_40" not in answers):
                jump Kazuki_1j_essay_stop
            # logic block, yes--> [more, stop, lazy]
            if("lily_essay_2_yes" in answers):
                jump Kazuki_1j_essay_more
            elif("lily_essay_2_no" in answers):
                jump Kazuki_1j_essay_stop
            else:
                jump Kazuki_1j_essay_lazy
        "No":
            $ addAnswer("lily_essay_1_no")
            jump Kazuki_1j_essay_no
        "...":
            $ addAnswer("lily_essay_1_no")
            jump Kazuki_1j_essay_what

label Kazuki_1j_essay_yes:
    mc "I suppose that I wouldn't mind the help."
    li "Are you sure your pride can take it?"
    mc "Hm? Take what?"
    li "Oh, just the fact that you're going to be getting English help from a 
        little girl."
    mc "Tiny would be the better word, I would think."
    li "That's not very nice."
    mc "Had you been in grade school or something along those lines, then I'd be
        pissed. But a midget my age? Yeah, that's fine."
    li "Um... in that case, I'm leaving."
    mc "Hey now, that was just payback for your earlier jab. Really, I'm 
        grateful for the help."
    li "Sure, sure. Let's look at it, top-downwards..."
    nmc "Lilian quickly scanned through the first page of actual content."
    li "... Wow. \"In somewhat-general terms, your lectures are mostly composed 
        of senile ramblings.\" Really?"
    mc "Well... I'm not wrong."
    $ minutes = minutes + 5
    li "You said this was for Amnaki?"
    mc "Yeah. That's the one."
    li "Okay. Fine. You're not wrong."
    mc "Have I ever been wrong?"
    li "Statistically speaking, you probably were at one point. But even if 
        you're right, that isn't something you can write here."
    mc "So, what do I write?"
    doublespeak li mc "Complete and utter..." "Bullshit?"
    li "Well, I was going to say nonsense, but that works too!"
    mc "Okay, that isn't really my thing. Unless I'm pretending that I'm 
        well-prepared for a presentation or something."
    li "Perhaps it would be better to look at what you wanted to say, and then 
        reverse it. You know, something like 
        \"I'd like to explain why I managed to fall asleep during your extremely
        informative lecture\"."
    mc "... And the whole paper needs to sound like that?"
    li "Hey, you wanna make her happy, right?"
    mc "Actually, I would prefer it if she was preparing for suicide."
    li "All right then. You want to pass her class, right?"
    mc "Well, I suppose I really don't have much of a choice."
    li "Exactly. Now as for this next sentence..."
    $ triple_min(10)#3:02?
    $ points[4] += 2
    nmc "30 minutes later, we had... something. It certainly was an improvement 
         from what I had written by myself."
    $ essay_status = "bad_but_mostly_complete"
    nmc "But the sentences simply didn't flow. Near the end, we may as well have
         been writing something along the lines of 
         \"Amnaki, you are an engaging instructor. I should have paid attention.
         This class is useful.\" and so on."
    nmc "... In fact, that {i}is{/i} what we wrote for our concluding 
         paragraph."
    li "We did it!"
    mc "Ehh... Not really. Sure, there are 10 full pages of writing here, but 
        some of it is childish. I mean, 
        \"You'll be the center of my attention from now on\"... Come on."
    li "I didn't write that."
    mc "You did. I am not that creepy of a person."
    li "But you're scary!"
    nmc "Lilian is actually tearing up. Is my face that fearsome...?"
    li "Actually, you're kinda cute! Like a super thin teddy bear!"
    mc "..."
    li "Hee hee! Messing with you is fun."
    nmc "I honestly couldn't tell if she was messing around or not, but for the 
         sake of my sanity, I decided to let the comment 
         slide."
    mc "Whatever... hang on. Don't you have to be somewhere? I imagine that 
        you're quite busy..."
    $ minutes = minutes + 3#3:05
    $ domchange("FP", -2, 0)
    li "Me? No, not really. I mean, I've got time. Why? Do you want to work on 
        this more, or would you rather call it quits?"
    # if mc indicated that he isn't interested in the 40 we're making him say no
    if("self_40" not in answers):
        return #line180
    $ cd_set(15, 15, 'return_stub')
    show screen countdown
    menu:
        extend ""
        "Yes":
            $ addAnswer("lily_essay_2_yes")#jump Kazuki_1j_essay_more
        "No":
            $ addAnswer("lily_essay_2_no")#jump Kazuki_1j_essay_stop
        "...":
            pass
    return #line244
    
label Kazuki_1j_essay_no:
    $ points[4] += -2
    mc "No thank you. Honestly, I should probably get to work. I'm already late
        as it is."
    nmc "I save the file and close the window. Not that there was a lot of 
         progress to save. I suppose 3 pages in 30 minutes isn't horrible."
    mc "I'm actually already running a little late."
    li "Oh. In that case, I might as well head home myself. Do you want a ride?"
    mc "Umm, I certainly wouldn't say no to a lift, but are you sure?"
    li "Actually, I insist."
    nmc "As she pulls me by the hand, it occurs to me that I've never actually 
         seen Lilian drive."
    mc "Hey, just out of curiosity, for about how long have you had your 
        license?"
    li "Not telling!"
    mc "Please, please tell me that you aren't about to do something illegal."
    li "Okay. I won't tell."
    nmc "Against my better judgement, I follow her out to the parking lot..."
    $ triple_min(5)
    li "All right, we're here!"
    mc "..."
    li "Wakey wakey, lemon cakey. You said Robert and Son's, yeah? This is the 
        place..."
    mc "I was ready to die..."
    nmc "I'm not exactly devout, but I was actually praying during Lilian's 
         little excursion."
    li "Is my driving really that bad?"
    mc "It's generally considered \"bad\" when you aren't in the correct lane."
    li "I was passing."
    mc "You were a solid 20 miles per hour over the speed limit."
    li "Better than being late, right?"
    mc "Considering that we didn't get a ticket, I suppose that I should be 
        thankful, yes."
    nmc "I decide not to tell her that I'm still late, although certainly less 
         late than I would have been without her."
    li "Darn right! Well, I'll catch you later."
    nmc "With that, she heads back to the car. The thought of her being on the 
         road is enough to make me reconsider getting my own license. Not that 
         I could afford a car."
    nmc "... In any case, time to face the music of Robert's wrath..."
    jump Kazuki_1k_work_alt # 2:42 PM
    
label Kazuki_1j_essay_what:
    nmc "I lazily stare back at the small girl in front of me. There is really 
         no need for me to answer."
    li "Ah, I suppose I'll take that as a \"no\" then."
    nmc "Turning my head towards the eggshell-white ceiling, I slightly slump 
         into my chair to show my lack of care."
    li "Alright! Well, best of luck!"
    nmc "Perfectly understanding my desires, Lilian happily skips away from my 
         table."
    nmc "... I should probably head to work now... I guess I have to take the 
         bus."
    $ triple_min(5)
    jump Kazuki_1k_work_alt # 2:42 PM

label Kazuki_1j_essay_more:
    $ points[4] += 2
    mc "Yes."
    li "Whaa!?"
    mc "You heard me. \"Yes.\"\n"
    extend "As in, \"yes, I am desperate\"...\n"
    extend "or \"yes, you have been helpful, believe it or not\"...\n"
    extend "or even \"look, I really want to get this garbage assignment out of 
            the way\"."
    li "I didn't hear a \"yes\" in that last one."
    mc "Look, you've been very helpful so far. Please, help me finish this 
        freaking thing!"
    li "Haha, okay. So, the sentences don't really transition into each other, 
        but they do outline what needs to be said. And we're still a few pages 
        short of the 10 we need..."
    $ triple_min(5)
    $ essay_status = "done"
    mc "We... We actually have something reasonable now..."#3:20PM
    li "Is that all of the homework that you had for today?"
    mc "Ehh. There's the actual math homework but that can be done over the 
        weekend. There's no physics homework since we have that test coming up."
    li "Oh, I see. I guess you don't need me anymore."
    mc "I suppose I don't."
    li "... We could get lunch."
    mc "Yes. We could."
    li "Err. I'm implying that you're welcome to join me for lunch."
    nmc "... The issue here is that I'm relatively broke. I need to save about 
         $800 a month in order to pay for the apartment. Suffice it to say that 
         I haven't exactly met that quota yet."
    li "Hey, if it's the money that you're worried about, I wouldn't mind 
        treating you."
    nmc "... Can I do that to her? Now that I think about it, we don't know each
         other all too well, and I have absolutely no idea how well off she is."
    $ cd_set(12, 12, 'Kazuki_1k_lunch_route')
    show screen countdown
    menu:
        extend ""
        "I'll pay for myself":
            $ addAnswer("lily_lunch_1_pay")
        "Accept her offer to pay":
            $ addAnswer("lily_lunch_1_treat")
        "Don't go to lunch with her":
            $ addAnswer("lily_lunch_1_bye")
        "...":
            $ addAnswer("lily_lunch_1_silence")
    $ jump_break()#really?
    jump Kazuki_1k_lunch_route#3:20PM

label Kazuki_1j_essay_lazy:
    $ addAnswer("lily_essay_2_what")
    nmc "... I stared blankly at the laptop screen."
    mc "Uhh..."
    $ jump_break()
    return

label Kazuki_1j_essay_stop:
    mc "No, that won't be necessary."
    nmc "I save the file and close the window."
    li "Ooh. Kazuki's a quitter! Kazuki's a quitter!"
    mc "Grr... In all seriousness, I think I've taken enough of your time."
    li "Actually, that works out well. I haven't had lunch yet."
    "{i}Grumble...{/i}"
    nmc "Now that my stomach reminds me, I haven't had anything to eat since 
         this morning myself."
    li "..."
    nmc "By now, the school cafeteria has probably stopped serving lunch."
    li "..."
    nmc "I didn't pack a lunch today, either."
    li "...!"
    nmc "I wonder what I could do for a-"
    li "{size=40}Hey! I'm talking to you!{/size}"
    nmc "I'm already fairly late for work... missing a day of work would 
         certainly be unusual for me, but it probably wouldn't hurt."
    mc "... Well, fuck me."
    li "Aha, I'd rather not. But what's up?"
    mc "I'm late for work!"
    li "E-Eh!? What do you mean?"
    mc "We somehow got carried away working on the essay. So carried away, that 
        I didn't realize how much time had passed!"
    li "What do you mean by \"we\"? Ooh, how could you be so careless?"
    mc "Oh, never mind. It doesn't really matter."
    li "Doesn't really matter?! Listen to yourself! Uurgh. This is why you don't
        have any friends."
    mc "That... hurt. A lot."
    nmc "Lilian probably has a point here. My lack of care does seem to turn 
         people away."
    li "I'm kidding. Anyway, thanks for keeping me company today."
    mc "Uhh, I didn't actually do you any favors."
    li "Still. This was nice."
    mc "Well, I'm glad that you thought so... Actually, now that I think about 
        it, I don't necessarily have to go to work..."
    li "Oh, yes you do. I'll talk to you later then."
    mc "Ahh, okay. See ya."
    nmc "... I guess I have to take the bus."
    $ triple_min(3)
    jump Kazuki_1k_work_alt#3:14 -- make a new jump-to
    
label Kazuki_1k_lunch_route:
    if hasAnswer("lily_lunch_1_silence"):
        $ removeAnswer("lily_lunch_1_silence")
        li "Aww, are you too sleepy for a late lunch?"
        mc "In a way... It's been a long day."
        li "Tell you what. Take a nap in the car."
        mc "... Do what?"
        li "It's a 10 minute drive, anyway. I think it would do you some good."
    elif hasAnswer("lily_lunch_1_bye"):
        mc "I think I'm going to have to turn you down."
        li "Oh?"
    if hasAnswer("lily_lunch_1_bye"):
        mc "It's... It's been a long day, and even if I were to skip lunch, I'd 
            still need to get to cross-country later. It'd be best for me to not eat
            anything."
        nmc "My out-of-the-ass reply seems to have made some sense, as Lilian nods 
             in response."
        li "Ah, I see. Well, thanks for keeping my company today. This was nice."
        mc "You helped me more than I helped you."
        li "I suppose that's true... Anyway, I'll let you get some rest. See ya."
        $ sn_draw("sn jaane")
        mc "Jaa ne."
        nmc "As Lilian skips off, I realize that I'm going to have to walk to 
             work..."
        jump Kazuki_1k_work_fail
    jump Kazuki_1k_lunch_lily

label Kazuki_1k_lunch_lily:
    if hasAnswer("lily_lunch_1_pay"):
        mc "I can pay for myself. Where are we going?"
    if hasAnswer("lily_lunch_1_treat"):
        mc "My wallet has been hurting lately. I certainly would appreciate that."
        li "Oh? What's up?"
        nmc "There's no need to inconvenience her with how I pay for - on top of the
             apartment rent - my father's bar tab, living expenses, and bail 
             whenever he gets into trouble. Although he's been pretty good with the 
             law lately."
        mc "Ehh, I've been having a hard time keeping up with the bills lately is all."
        nmc "... Technically true."
        li "Ahh, okay. I'll have to take you somewhere nice then."
        mc "What do you have in mind?"
    li "Oh, you'll see. Come on. You haven't seen my car yet."
    mc "I'm more concerned with where we're going than how we're getting there. 
        And I haven't seen your license, either."
    li "They're both surprises!"
    nmc "Lilian leads the way to the parking lot..."
    $ minutes += 3
    $ sio_l("bg parkinglot1")
    li "Here we are!"
    show framed lilian car1:
        xalign 0.5 yalign 0.3
    mc "Uhh... Wow."
    nmc "Due to my job as a machine shop aide with Robert, I thought I would be 
         more familiar with car makes and models. But this..."
    mc "... This doesn't look like it'll even start..."
    nmc "Well, I've been around cars enough to know that appearances aren't 
         everything. But given that the front bumper is missing, I'd wager that 
         this car has been through some rough times."
    mc "I... I'm pretty sure that you can't legally drive this thing."
    li "I'm licensed. Isn't that enough?"
    mc "Where is your car's front bumper?"
    li "Oh. I don't actually know... Well, it all happened so fast!"
    mc "What kind of accident would rip the front bumper out of your car, 
        but not put you in the hospital?"
    li "Heh. I was put in the hospital, alright."
    mc "... So when are you getting your car fixed?"
    li "Eh, it'll get fixed when it gets fixed."
    mc "... You know I work at an auto repair shop."
    li "If it still works, it ain't broke. Well, get in!"
    menu:
        extend ""
        "Ask about insurance":#well it's what Kazuki would do...
            mc "What will happen when we get in an accident?"
            li "Well, I'm guessing that someone is going to get hurt. Hopefully not one 
                of us."
            nmc "... She agrees with me? We {i}are{/i} getting in an accident 
                 at {i}some{/i} point?"
            mc "No, I mean, are you and your car insured?"
            li "Again, I don't know. So, are we going to lunch or not?"
            menu:
                extend ""
                "Sounds like fun":
                    jump Kazuki_1k_hell_yes
                "Not a good idea":
                    jump Kazuki_1k_hell_no
        "Sounds like fun":
            jump Kazuki_1k_hell_yes
        "Not a good idea":
            jump Kazuki_1k_hell_no
    return

label Kazuki_1k_hell_yes:
    mc "Okay, \"why not\", I suppose."
    li "Really?"
    mc "Sure. I could use some fun, every now and then."
    li "Right. Because you're just a blinding rainbow of happiness."
    nmc "She's joking, but I really don't have the best of dispositions."
    mc "... I still think you should get this car fixed as soon as possible."
    li "You're just saying that because you're a mechanic."
    mc "Who said that I was a mechanic?"
    li "A hummingbird told me that you work at Robert and Son's. Did it lie?"
    mc "Well, no... But I just do paperwork there. Really."
    li "Boo! You're useless!"
    mc "... Were you thinking that I'd fix the car if you bought me lunch?"
    nmc "She says nothing, but looks at her feet with a smirk."
    mc "How'd I guess?"
    li "Maybe you know me better than you think."
    mc "Whatever."
    #~car transition~
    mc "..."
    li "..."
    nmc "Well, to break the monotony, I think I'll ask about..."
    $ cd_set(15, 15, 'Kazuki_1k_mid_drive')
    show screen countdown
    menu:
        extend ""
        "The car":
            $ addAnswer("lily_drive_1_car")
            pass
        "The restaurant":
            $ addAnswer("lily_drive_1_restaurant")
            pass
        "...":
            $ addAnswer("lily_drive_1_nothing")
            pass
    jump Kazuki_1k_mid_drive

label Kazuki_1k_hell_no:
    mc "... Yeah, this doesn't seem like a good idea."
    li "Hmm? Why not?"
    nmc "I could think of several reasons. I don't want to mess with a friend's 
         love interest. I don't want to get into a car when Lilian is driving. 
         The restaurant might be serving French food for all I know, which I 
         really can't stand."
    nmc "I can't say any of that. But I can say..."
    mc "Feeling-funny-bye."
    nmc "And I ran off. Juvenile? Yes. Viable? Also yes."
    nmc "As Lilian fades into the distance , I realize that I'm going to have 
         to walk to work..."
    jump Kazuki_1k_work_fail

label Kazuki_1k_mid_drive:
    if hasAnswer("lily_drive_1_car"):
        mc "So, for how long have you had this clunker?"
        li "Well, I got it from my father. He got it from his mother, who 
            got it from her brother who..."
        mc "No, really."
        li "A week."
        mc "... Really?"
        li "Yeah. My big sister drove it up here while she was visiting, 
            and she forgot to take it home."
        mc "Bullshit. Who forgets their car?"
        li "I mean... Remember that time I went to school without my shoes?"
        mc "Your feet were featured in the school paper, Lilian. Are you telling me 
            that forgetfulness runs in the family?"
        li "I'd rather blame my parents than myself! But yeah, I really think it does."
    elif hasAnswer("lily_drive_1_restaurant"):
        nmc "... She won't tell me where we're going, but I wonder if she'll 
             tell me what kind of food we'll be having."
        mc "So... where we're going... you're sure you want that to be a surprise? 
            What if I'm allergic?"
        li "I think if you had allergies, you'd be a pickier eater."
        nmc "She's right. I don't have any food allergies that I know of, and I'll 
             eat just about anything. But how can she be so certain about my diet?
             We don't eat together very often."
        mc "You keep track what I shove in my mouth?"
        li "Well no, but every time I've seen you order food from the City Cafe, you 
            kind of just... randomly pick something."
        nmc "Okay, I do that, it's weird, fine, anyone would notice."
        mc "You're right. To my knowledge, I'm allergy-free."
        li "Good to know!"
    else:
        $ addAnswer("lily_drive_1_nothing")
        nmc "Actually, I'll just let her drive."
        li "You look tired."
        mc "Eyes on the road!"
        li "Sheesh. Sorry. But you look tired. And a little beat-up."
        nmc "My thoughts wander to this morning's mini-adventure... sharing 
             what happened would probably be a bad idea."
        mc "Yeah. My uhh, cat decided that my face was comfortable. And my cat 
            had gas. Ugh."
        nmc "I don't have a cat."
        li "I thought you didn't have any pets?"
        nmc "Shit."
        mc "And that was a problem. So I fixed the problem by getting a cat."
        li "Oh. So what does cat fart smell like?"
        mc "Rotten beans."
        li "Sounds lovely."
    $ minutes += 4
    extend " Hey uhh, these next few roads are sort of... hard for me, so I need you 
            to shut up for a sec."
    mc "No problem."
    nmc "If she's as bad as a driver as she let's on, she seriously needs to 
         concentrate. Okay, that's fine."
    nvlmc "... I still don't understand. Why is she being so kind to me, and why now? 
           There must be something that she wants from me."
    nvlmc "Something more than just assistance with LAST, or companionship."
    nvlmc "Conflicted, negative emotions pierce my mind like pins in a pincushion."
    nvlmc "What she wants... is it loyalty? A secret keeper?"
    #?
    return

label Kazuki_1k_post_drive:
    "Waiter" "Hello again, Lilian. More than one this time, huh?"
    li "Yup! For two, please!"
    "Waiter" "Excellent. Right this way."
    nmc "The waiter sits us down at a window table, fills our water glasses, 
         hands us menus, and leaves."
    mc "... I can see why this is your favorite restaurant."
    li "Oh, can you?"
    nmc "The decor is very well done. Not fitting for a Thai restaurant, but 
         tasteful regardless."
    nmc "Jade pendants and lit Chinese lanterns are hanging from the wall."
    nmc "A number of distinct smells waft through my nose."
    nmc "Cilantro, tumeric, ginger, mustard, coconut, chicken stock... All the 
         way from the main entrance. I couldn't even see the kitchen from where 
         I was standing."
    nmc "High-quality stuff. Fresh stuff. I think. I don't spend as much time in
         the kitchen as I would like."
    nmc "But of course, I didn't say any of this."
    mc "Yes, I can."
    li "Well, then that's one more thing we have in common."
    mc "Oh? We have more than one thing in common?"
    li "We're both human!"
    mc "I was hoping for something slightly more... ground-breaking."
    li "In that case, I've got nothing."
    return

label Kazuki_1k_work_fail:
    call impossible_problem_1
    $ minutes += 30
    ro "What the fuck clock in the bloody afternoon do you call this, you filthy
        piece of... You lazy dickwad."#3:50PM
    nmc "... The man is not known for his clean language, nor for his creativity."
    mc "Yes, I'm late. I'm sorry."
    ro "You know, back in my day, we were never actually late to work. Instead, 
        we didn't show up. Because we knew what would happen if we went to work.
        We'd be fired."
    mc "... Am I being let go?"
    ro "No, but I'm royally pissed off and I'm sending you home."
    nmc "Robert wasn't known for his leniency either, but on most other days 
         he's slightly more patient."
    mc "Yes sir. Sorry sir."
    nmc "As I turn my back, I realize that I'm going to have to walk home..."
    return

label Kazuki_1k_work:
    # 2:00PM
    $ minutes = 840
    call impossible_problem_1
    # alternate intro to robert hale
    $ sio_l("bg workshop")
    $ minutes = 870#2:30
    ro "Blasted self-entitled good-for-nothing ignorant plebeian consumerist 
        sheep people cunt dicks."
    nmc "... The man is not known for his clean language."
    mc "Mr. Hale?"
    nmc "Robert Hale has been the proud owner of Robert and Son's Machines for 
         as long as anyone can remember, which is of course, not very long at 
         all. This in itself is a bit awkward, since Robert lost custody of his 
         son when he was divorced. But changing the name of his little shop 
         would be an expensive pain in the ass in terms of both paperwork and 
         physically changing the sign, so the name stuck."
    extend "\nHis words, not mine. There have been a few awkward moments though,
            when I have been mistaken as his son..."
    nmc "Moments like those remind me of Robert's Irish descent."
    mc "Excuse me, Mr. Hale?"
    ro "That bitch Rachel called again."
    nmc "Rachel made the mistake of trying to get her cell phone repaired here. 
         Not that we couldn't have repaired it, but she insisted that we repair 
         the phone for free and deliver the repaired phone on the same day the 
         phone was brought in."
    nmc "In any case, I happen to work for Mr. Hale. Three hours a day, by the 
         sweat and grime of my brow, wrench in hand... actually I just handle 
         the taxes, the telephone, and the computers."
    mc "She's still alive?"
    ro "Well her driver's license says that she's 84."
    mc "Didn't you say she was your first customer?"
    $ minutes = minutes + 2
    ro "Yep. Good ol' days, eh?"
    mc "Umm. I find it unlikely that I was even alive back then."
    ro "I suppose that would be unlikely yes. How old are you again? Twelve?"
    mc "Robert..."
    nmc "Our senses of humor are not exactly compatible."
    ro "Heheh. Anyway, I've got work for you."
    nmc "He points at the workstation."
    mc "Oh! Is the computer broken?"
    ro "No. The assholes have started scheduling appointments through e-mail."
    mc "Ah. I see."
    ro "You know what to do. I need a nap."
    mc "Pardon?"
    ro "You heard me. G'night."
    $ sio_l("bg blackdrop")
    call triple_min(15)
    $ sio_l("bg workshop")
    nmc "... Okay, this is actually hard."
    nmc "The issue here is that I am looking at the appointments detailed in 
         emails, and trying to put these into the calendar At the same time, I 
         am taking phone calls, and putting those vocalized appointments into 
         the calendar."
    nmc "Multitasking is normally one of my stronger suits, but not when all of 
         my work is being done on the same peripheral."
    nmc "... This would actually be much easier if I had two computers and a 
         tablet."
    mc "Hello, Robert and Son's Machines. Yes, we can service your Hyundai. 
        Certainly, I can schedule you for Monday. Give me a moment. Oh, you said
        an Audi for Friday? My mistake. One moment. Okay, you are all set for 
        Wednesday. Oh my God, I am so sorry. Audi. Friday. Got it. Thank you for 
        your business."
    nmc "My shift wore on, with most of the calls sounding like that."
    jump Kazuki_1l_work

label Kazuki_1k_work_alt:# 2:42 PM or 3:05
    #$ minutes = 882
    $ sio_l("bg workshop")
    nmc "Robert Hale has been the proud owner of Robert and Son's Machines for 
         as long as anyone can remember, which is of course, not very long at 
         all. This in itself is a bit awkward, since Robert lost custody of his 
         son when he was divorced. But changing the name of his little shop
         would be an expensive pain in the ass in terms of both paperwork and 
         physically changing the sign, so the name stuck."
    extend "\nHis words, not mine. There have been a few awkward moments though,
            when I have been mistaken as his son..."
    nmc "In any case, I happen to work for him. Three hours a day, by the sweat 
         and grime of my brow, wrench in hand... actually I just handle the 
         taxes, the telephone, and the computers."
    mc "Apologies for the tardiness, Mr. Hale."
    ro "Infernal self-entitled crap-infested ignorant plebeian capatalist 
        scum-of-the-earth bitch."
    nmc "... The man is not known for his clean language."
    mc "Umm. Mr. Hale?"
    ro "That bitch Rachel called again."
    mc "I see. That would certainly explain the swearing."
    nmc "Rachel made the mistake of trying to get her cell phone repaired here. 
         Not that we couldn't have repaired it, but she insisted that we repair 
         the phone for free and deliver the repaired phone on the same day the 
         phone was brought in."
    nmc "A ridiculous customer by all accounts. So basically, everyone in the 
         office hates this customer more than any other."
    mc "I'm sorry that I wasn't here to take the call."
    nmc "Robert, for all of his years, is worse with people than I am, and has 
         an incredibly hard time just hanging up on a customer. I normally 
         curse out Rachel and put down the receiver, not giving her a chance 
         to make any demands."
    ro "Yeah, about that. Tell me why you weren't here on time again?"
    mc "Well..."
    $ cd_set(15, 15, 'Kazuki_1k_work_mum')
    show screen countdown
    menu:
        extend ""
        "Amnaki":
            $ addAnswer("work_excuse_amnaki")
        "Lilian":
            $ addAnswer("work_excuse_lilian")
        "...":
            jump Kazuki_1k_work_mum
    jump Kazuki_1k_work_excuse
    
label Kazuki_1k_work_mum:
    $ points[5] += -4
    $ addAnswer("work_excuse_none")
    nmc "I can't actually think of a reasonable excuse, so I say nothing."
    ro "... Whatever. Get to work. I'm taking a nap."
    jump Kazuki_1k_work_excuse
    
label Kazuki_1k_work_excuse:
    $ points[5] += -2
    $ tempsay = "I bitch to Robert about school on a fairly regular basis, and \
even if I didn't, he keeps in contact with some of the faculty \
anyway. So he kind of knows most of the teachers and students \
that I see on a regular basis."
    if("work_excuse_amnaki" in answers):
        mc "Amnaki gave me one of her \"assignments\"."
        ro "Oh. How many pages?"
        mc "Ten."
        ro "I see."
        nmc "[tempsay]"
        ro "Well, we weren't busy today, so it isn't too big of a deal. Get to work 
            now. I'm taking a nap."
    if("work_excuse_lilian" in answers):
        mc "I was working on a paper with Lilian, and I lost track of the time. I'm 
            sorry."
        nmc "[tempsay]"
        ro "Make sure it never happens again. Or so I'd say, but this isn't your
            first time being late. You screwed her afterwards though, right?"
        mc "What? No."
        ro "Hmph. Whatever. Get to work. I'm taking a nap."
    jump Kazuki_1l_work
    
label Kazuki_1l_work:
    $ sio_l("bg workshop")
    $ minutes = 1005
    #4:45PM
    nmc "Robert wobbles into the room, clearly drowsy. I am just now putting in 
         the last of the appointments."
    mc "Were you actually able to get some sleep?"
    ro "Enough."
    nmc "He says as he trips over absolutely nothing."
    mc "... Are you sure?"
    nmc "Robert picks himself up off of the floor and shakes his head as he 
         answers."
    ro "No, but I'll live. How's the work coming along?"
    mc "Nearly all of the appointments are in your system. Next Tuesday will be 
        busy for you."
    ro "Hmm. You did that a lot faster than I thought you would."
    mc "Considering that your expectations are generally low..."
    ro "\"Blessed is the man who expects nothing, for he shall never be 
        disappointed.\""
    $ cd_set(7, 7, 'Kazuki_1l_work_minus')
    show screen countdown
    menu:
        extend ""
        "Mark Twain?":
            mc "Was it Mark Twain that said that?"
            ro "No. It was actully Alexander Pope."
        "Alexander Pope?":
            mc "That sounds like an Alexander Pope quote." 
            ro "It was indeed him who said it."
        "Oscar Fingal O'Flahertie Wills Wilde?":
            mc "That sounds like Oscar Fingal O'Flahertie Wills Wilde."
            ro "Who?"
            mc "You know. Oscar Wilde?"
            ro "No... no I don't know."
            mc "Never mind. So it wasn't Oscar Wilde who said that?"
            ro "No, it was actually Alexander Pope."
        "...":
            jump Kazuki_1l_work_minus
    jump Kazuki_1l_work_extend

label Kazuki_1l_work_minus:
    ro "Give up? Alexander Pope said that. He was a good man."
    mc "It sounds like you knew him."
    ro "I'm not that old... He died in 1744."
    jump Kazuki_1l_work_extend

label Kazuki_1l_work_extend:
    mc "So you're telling me that you didn't expect me to get anything done?"
    ro "Correct. And I was, in turn, impressed."
    ro "Well in any case, here's your check for the day."
    if("lunch_work_1" in answers):
        $ main_char_cash = main_char_cash + 80
    if("lunch_essay_1" in answers):
        $ main_char_cash = main_char_cash + 40
    if(essay_status == "done"):
        $ main_char_cash = main_char_cash + 50
    mc "Sir? This isn't a check. This is cash."
    ro "Check, cash, money order, gift card, same thing."
    mc "I really don't think that finances work that way."
    ro "Sure they do. Money is money."
    mc "If you say so. Thank you."
    ro "I'm closing up, now. Get out of here."
    jump Kazuki_1m_routing

label Kazuki_1m_routing:
    return