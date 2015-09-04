# crashes as we know them

# PlaceholderX
# because these images don't exist, we want PlaceholderX to crash
#    image bg cafeteria9 = PlaceholderX("drops/eggs.png", "drops/cafe1.png", pretext = "(PLACEHOLDER) ")

# lib_music
# because we are using more than one mlib instance, we want lib_music to crash
#init:
#    $ break_renpy = mlib_space()

# Ren'PY itself
# missing https://pypi.python.org/pypi/lupa
#init python:
#   import lupa
#   L = lupa.LuaRuntime(unpack_returned_tuples=False)
#   luaCode = file(config.gamedir + "/Scripts/hello.lua").read().decode("utf-8")
#   L.execute(luaCode)
##test with L.globals().message
