label impossible_problem_lead1:
    $ nmc = Character(None, what_style="main_gray")
    $ showMCStatus = False
    jump impossible_problem_1

label impossible_problem_1:
    nmc "On the half-hour walk to Robert and Son's Machines, I realize that I 
         have some time to think about problems. Specifically variants of 
         impossible problems."
    show asset chessboard initial:
        xalign 0.5 yalign 0.35
    nmc "Consider for a moment, the Mutilated Chessboard Problem, as posed by 
         Martin Gardner. Although, I would have called it the 2-by-1 Corner 
         Truncation Problem."
    hide asset chessboard initial
    show asset chessboard dominoed:
        xalign 0.5 yalign 0.35
    extend " The premise of the problem is that an unmodified 
            chessboard can clearly be completely covered by a number of standard 
            dominoes."
    nmc "Of course, this is assuming that you place a domino over two adjacent 
         squares and don't do anything silly, like placing a domino diagonally, 
         using oversized dominoes, breaking dominoes in half, dangling dominoes 
         off of the board's edge, and so on."
    hide asset chessboard dominoed
    show asset chessboard cut:
        xalign 0.5 yalign 0.35
    extend " If you remove two white squares on the board however, can you still
            fill the chessboard with dominoes?"
    nmc "The answer is, of course, no. While it's certainly true that removing 
         these spaces still leaves the board with an even number of squares... 
         well."
    hide asset chessboard cut
    show asset chessboard issue1:
        xalign 0.5 yalign 0.35
    nmc "A domino placed with these restrictions must cover both a black and a 
         white square. If the ratio between the quantity of black squares to 
         white squares is anything but one-to-one, this is evidently 
         impossible."
    hide asset chessboard issue1
    show asset chessboard initial2:
        xalign 0.5 yalign 0.35
    nmc "But what happens if I remove a black tile and a white tile? Does it 
         matter which tiles I remove? And can I then fill the board with 
         dominoes?"
    hide asset chessboard initial2
    show asset chessboard solved2:
        xalign 0.5 yalign 0.35
    nmc "The answer to this new problem is yes, that I will always be able to 
         fill the board regardless of the two removed tiles. Additionally, the 
         proof is still somewhat geometric. "
    hide asset chessboard solved2
    show asset chessboard rook1:
        xalign 0.5 yalign 0.35
    extend "Imagine how a rook would travel through the board, and realize that 
         its movement pattern must alternate tiles: black, white, black, white, 
         and so on. A single path is not necessarily guaranteed if these two 
         tiles are removed."
    hide asset chessboard rook1
    show asset chessboard rook2:
        xalign 0.5 yalign 0.35
    nmc "So what? Picture the removal of a black square. A single rook may still
         traverse the entire board, but both starts and ends on a white square."
    hide asset chessboard rook2
    show asset chessboard rook3:
        xalign 0.5 yalign 0.35
    nmc "Then remove any white square. If we remove one of the end squares, then
         we've presented the problem in an incredibly stupid manner, and have 
         just asked \"well what happens if we remove a domino's worth of 
         squares\"."
    hide asset chessboard rook3
    show asset chessboard rook4:
        xalign 0.5 yalign 0.35
    nmc "Remove a white square in the middle though, and we absolutely create 
         two paths. Black at the start and white at the end. Traversable paths 
         with different ends. "
    hide asset chessboard rook4
    show asset chessboard rook5:
        xalign 0.5 yalign 0.35
    extend "Quod erat demonstrandum."
    hide asset chessboard rook5
    nmc "But what if we tried to solve the problem in a non-geometric manner? 
         Hmm..."
    return

label impossible_problem_2:
    nmc "I suppose that I have time to consider another impossible problem."
    nmc "It had always been presented as the \"Light Faster than Light\" 
         problem in textbooks and scientific papers, but I had never bothered 
         to give it any thought."
    nmc "Let's say that you're travelling at the speed of light - or for the 
         sake of argument, damned near close to it - and if you held a 
         flashlight behind you, then what would you see?"
    nmc "Technically impossible since one can't move at the speed of light."
    nmc "But for the sake of the problem, let's say that this is happening on 
         the Earth. Relatively (haha) soon, you'll the beam of light would pass 
         you as if you weren't actually moving at all."
    nmc "\"I thought I wouldn't be able to see the light at all!\" or \"I 
         thought the beam would be moving twice as fast!\" come to mind as 
         counter arguments, but spacial relativity dictates that time dilation 
         must be taken into account."
    nmc "Along the same lines, what if I was pointing the flashlight in front of
         me, rather than behind?"
    nmc "In that case, the car would serve as the point of reference. So nothing
         in the car would be different."
    nmc "But as the light bounces off of the environment and is reflected 
         towards your eyes, everything would... wait a second."
    nmc "The environment is moving towards me at the speed of light, so the 
         Doppler effect would actually come into play."
    nmc "So... everything would be shifted towards the ultraviolet or beyond."
    nmc "Not that I know what that would look like."
    return
