label Kazuki_1a_else:
    $ dev_screen = "pass"
    window hide
    #show screen fake_say
    #[scene1
    $ clock = False
    $ walletshow = False
    $ main_char_show_rpg = False
    scentered "Episode 0: Understanding"
    $ clock = True
    $ walletshow = True
    $ main_char_show_rpg = True
    $ mlib("march")
    #window show
    scene bg fakefog
    with dissolve
    scene bg fog
    nnvlmc "This is my world. It is eerie, cold, and isolated."
    nnvlmc "Eerie enough that the shadows themselves are unsure of where to go."
    extend " And so cold... I can't feel myself shiver."
    extend " The isolation. I myself don't belong here."
    nnvlmc "Despite this, there is neither the feeling of pain nor that of bliss. I merely exist, and wander through the fog. Fog so thick that I could drink it..."
    extend " Pain can only last for so long. The hatred I have felt would have killed a weaker man."
    nnvlmc "I don't understand love. I have never experienced it, and I cannot recognise it."
    extend " Perhaps I had once known how to love, and love well. But those I could love have since left me."
    nnvlmc "Even so, I live. For what else am I to do but join the world in its cycle? The tumultuous cycle in which there is no true chain of command."
    nnvlmc "Left, and right. Left, and right. Despite my qualms, these uncovered feet of mine take me forwards."
    extend " Towards where, as always, is a matter of negligible significance. He who wanders is he who is waywards."
    extend " My final destination, whether it be nearby or otherwise, is not known to me."
    nnvlmc "Is this depression? Or simply a failure to fit in?"
    extend " This is my world, but I know neither where I will go nor where I am."
    nnvlmc "I walk past a vision of my family."
    nnvlmc "Is that how my mother appeared when she died?"
    extend " Did my father truly once know how to smile?"
    extend " Was I truly an only child?"
    nnvlmc "My questions echo through the space around me, but I did not speak."
    nvl clear
    nnvlmc "...{w} ...{w} ..."
    nnvlmc "I knew right away... I had known... that this wasn't a dream.{w} That's not to say that it felt too real to be a dream. On the contrary, it felt too unreal 
            to be a dream."
    nnvlmc "Someone else's thoughts and feelings... perhaps someone that I had once known... they were overpowering my own, to the point that I couldn't think or feel for myself. And there
            was nothing. Nothing at all. Nothing but a dull marching."
    nnvlmc "I am describing someone else's world. {w}This is not truly my world, nor the world that we humans live in. {w}Someone else is controlling this place..."
    nnvlmc "Yes, a dull marching and a perfect darkness. I couldn't see, smell, taste, nor touch - only hear."
    nnvlmc "I couldn't move, nor could I breathe. {w}I could do nothing but merely exist.{w} Thinking itself... it could only be done in forced fragments."
    stop music
    nnvlmc "And then the dull marching stops. I should be stressed and unsure of what is about to happen, but my body is relaxed."
    nnvlmc "The extraneous thoughts are cleared from my mind, but this only makes me more impatient."
    nnvlmc "I knew who I was, but who am I now? And what is to become of me?"
    nvl clear
    nnvlmc "The marching changes to a single pair of footsteps, and as if this new presence brought light with it, a dim light fills my eyes, and
            a shallow gust flows through my lungs.{w} And in front of me was a shadow, standing upright..."
    nvls "Stand."
    nnvlmc "My body stood up, ignoring my brain's demands to ask questions."
    nvls "See."
    nnvlmc "And then I realized then that I could in fact see. I was simply unable to process what I was seeing."
    nnvlmc "My body once more obeyed the shadowy voice. It belonged to an equally-shadowy body. I looked into its eyes, and I saw a void. And the void stared back."
    nvls "Feel pain. Remember me."
    nnvlmc "I received what felt like a punch to the stomach, even though the shadow did not move."
    call domchange("HP", -20, 1)
    extend " Pain surged through my nerves, but I did not budge nor gasp. My body refused to buckle under the burning rage of the shadow, as it had also been instructed to stand."
    nvls "Return."
    nnvlmc "And then the darkness covered my eyes, and I was returned to the world of the living..."
    scene bg fakefog
    nvl clear
    #]
    return