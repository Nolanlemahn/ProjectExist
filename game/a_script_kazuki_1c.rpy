label Kazuki_1j_skip:#we skipped lunch
    $ sio_l("bg workshop")
    nmc "Robert Hale has been the proud owner of Robert and Son's Machines for as long as anyone can remember, which is of course, not very 
         long at all. Which is a bit awkward, since Robert lost custody of his son when he was divorced. But changing the name of his little 
         shop would be an expensive pain in the ass in terms of both paperwork and physically changing the sign, so the name stuck."
    extend "\nHis words, not mine."
    nmc "In any case, I happen to work for him. Three hours a day, by the sweat and grime  my brow, wrench in hand... actually I just handle 
         the taxes, the telephone, and the computers."
    mc "Hello, Robert and Son's Machines. Yes, we can service your BMW. Yes, I can schedule you for Monday. Certainly. Good day to you too."
    $ minutes = minutes + 15
    $ sio_l("bg workshop")
    mc "Yes, Robert and Son's. No, we don't take walk-ins. No, the manager is actually working on a car at the moment. '99 Ford Explorer 
        actually, but... No, we are completely booked for Friday... We don't actually work on Saturday. Next Tuesday will work. Of course. 
        Enjoy the rest of your afternoon."
    $ minutes = minutes + 15
    $ sio_l("bg workshop")
    mc "Hello, Robert and Son's Machines. Fuck you too."
    nmc "Now normally, that sort of language would get me fired and could get me sued. However..."
    r "Kazuki, was that Rachel on the phone?"
    mc "Yes sir."
    r "What a bitch. Carry on."
    nmc "Rachel made the mistake of trying to get her cell phone repaired here. Not that we couldn't have repaired it, but she insisted that we 
         repair the phone for free and deliver the repaired phone on the same day the phone was brought in."
    nmc "A ridiculous customer by all accounts. So basically, everyone in the office hates this customer more than any other."
    r "Oh, how's tomorrow's schedule looking?"
    mc "Completely booked."
    r "And Monday's schedule?"
    call sn_label("sn siebener")
    mc "One car. A Siebener. Nothing else for Monday."
    r "I hate working on beemers. Tuesday?"
    mc "No cars at all. The whole week is basically empty, actually. I might not be needed for most of the week. Although I could still come in if 
        you'd like. Here, look at the schedule."
    nmc "There are very few schedules worse than an overbooked one. Because even if you are working overtime, you are still in fact working. 
         When we have an underbooked schedule, we spend a lot of time twiddling our thumbs and since our salaries are comission-based, we 
         also don't get paid as much."
    r "I didn't think it would be possible to have less business this week than last week. I'll have someone else do the phones on Tuesday. 
       Take Tuesday off."
    mc "You could show me how to repair something instead."
    r "Nope. You aren't licensed for... anything. Even if I did show you the insides of an iPhone, it would be all kinds of illegal for 
       you to do paid work. Unless you want to fix another coffee maker."
    mc "... I suppose I learned my lesson with the coffee maker."
    nmc "Robert was of course, referring to \"The Ground Problem\", or at least, that's what he calls it when he retells the story to customers. 
         Ground floor, ground coffee, haha."
    nmc "Although Robert is technically a mechanic, a few customers began to bring their computers to us. Originally, we told them that we didn't 
         have any computer parts. One Tuesday however, I told Robert to let me take a look at it, and as it turned out, the problem was between 
         the desk and the chair."
    nmc "\"My computer won't connect to the Internet!\" The problem wasn't the network interface controller, which is, of course, the thing that 
         the silly-looking blue wire goes in. The problem was actually with the settings on the operating system. Somehow, the computer was 
         trying to use Google as a router."
    nmc "... That's kind of like trying to use beef to fertilize the grass that cows eat. Which only makes sense if you know nothing about 
         farming. Ignoring the fact that some farmers do directly feed their livestock animal by-products. Which is basically bad beef."
    nmc "Anyway, I fixed the computer. The next day, I got admittedly cocky and tried to fix a coffee machine without telling Robert."
    nmc "Long story short, the carpet has a very large coffee stain in it."
    nmc "And so, I allowed another day of appointment scheduling and paperwork to drag on."
    jump Kazuki_1k_routing
    return  
    
label Kazuki_1j_lunch:#we're getting a bagel, lol ya right
    # 1:50PM
    $ sio_l("bg bus1")
    nmc "As I confirmed this morning, it takes 5 minutes to get to school if I sprint, trespass, pick a few locks, jump dangerously, and so on."
    nmc "But honestly, I'm not up for repeating all of that nonsense. So, I'm taking the bus home."
    $ sio_l("bg blackdrop")
    $ triple_min(2)
    nmc "The rest of the bus drive proceeded without incident."
    $ sio_l("bg kazuki kitchen")
    nmc "I let myself into the apartment and begin getting things out of the refrigerator."
    nmc "Father doesn't own a car. He had a Subaru, but then he sold it to pay off his tab. So I can't actually tell if he's home or not. 
         At least not just by walking through the front door."
    nmc "And honestly, I don't care enough to check on him."
    mc "Freaking why."
    nmc "While all of my smoked salmon was where I left it, someone had eaten the last bagel after I left for school."
    nmc "I suppose white bread will have to do."

label Kazuki_1j_essay:#we're writing an essay, lol ya right
    nmc "A 10 page essay on why I wasn't paying attention in class."
    nmc "\"Well gee, Ms. Amnaki, it may or may not have to do with your inability to teach things that are new to me.\""
    nmc "Mm, an excellent topic sentence."
    nmc "\"Additionally, due to the nature of your teaching style, all I need to do is briefly scan the 40' x 30' 
         Whiteboard to get a brief summary of the lesson. For instance, on the day that you gave me this assignment, you 
         were in the middle of a simple two-dimensional rotation problem...\""
    $ minutes = minutes + 2
    $ sio_l("bg library1")
    return

label Kazuki_1k_routing:
    $ sio_l("bg fog")
    $ minutes = 1070
    #first major branch of the common route;
    #we need to check for both the faculty thing and for the move natalie thing, which could be awkward
    if(("meeting_known" in answers) or ("meeting_hlawrence" in answers)):
        nmc "I'd better get to that damned meeting now."
    return