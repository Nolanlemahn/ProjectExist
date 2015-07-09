image empty = "drops/empty.png"

# miscellaneous, non-framed assets
image asset flier last = "assets/flier_last.png"
image asset chessboard initial = "assets/chessboard_initial.png"
image asset chessboard dominoed = "assets/chessboard_dominoed.png"
image asset chessboard cut = "assets/chessboard_cut.png"
image asset chessboard issue1 = "assets/chessboard_issue1.png"
image asset chessboard initial2 = "assets/chessboard_initial2.png"
image asset chessboard solved2 = "assets/chessboard_solved2.png"
image asset chessboard rook1 = "assets/chessboard_rook1.png"
image asset chessboard rook2 = "assets/chessboard_rook2.png"
image asset chessboard rook3 = "assets/chessboard_rook3.png"
image asset chessboard rook4 = "assets/chessboard_rook4.png"
image asset chessboard rook5 = "assets/chessboard_rook5.png"

# unframed versions of the assets
image unframed lilian car1 = PlaceholderX("framed/template.png", "framed/lilian_car1.png", tsize = 45, tcolor = "#FF0000", talign=(0.3, 0.5), pretext = "(PLACEHOLDER) ")

# framed, miscellaneous assets
image baseFrame = "framed/border.png"
image framed lilian car1 = LiveComposite((600, 450),
                                         (0, 0), PlaceholderX("framed/template.png", "framed/lilian_car1.png", tsize = 45, tcolor = "#FF0000", talign=(0.3, 0.5), pretext = "(PLACEHOLDER) "),
                                         (0, 0), Image("framed/border.png"))

# assets for pseudo UI elements
image world divide = "menus/WorldDivide.png"