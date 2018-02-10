init -1 python:
    import lupa
    lua = lupa.LuaRuntime(unpack_returned_tuples=False)
    def LuaExec(script):
        return lua.execute(GameRead(script))

    def LuaTest():
        return LuaExec("/LuaScripts/hello.lua")