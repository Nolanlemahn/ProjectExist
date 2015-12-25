python early:
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
    config.save_directory = "project-exist-1"
    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "README.html"

init -2 python:
    import os
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    config.windows_icon = "icon.png"
    config.window_icon = "icon.png"

    config.name = "Project Exist"
    config.developer = checkUserDev()
    config.keymap['save_delete'].append('K_BACKSPACE')
    config.fast_skipping = True

    config.window_title = "Project Exist"
    config.default_fullscreen = None
    config.gl_resize = False

    ## These values tell Ren'Py how to build a distribution.
    config.version = "v0.2.8_(1068)"
    config.log = os.path.abspath(config.gamedir + "/../debuglog.txt")
    build.directory_name = "ProjEx_" + config.version
    build.executable_name = "Project Exist"
    build.include_update = True
    build.classify('flowcharts/**', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('*.sh', None)
    build.classify('*.bat', None)
    build.classify("**.rpy", None)

    build.classify('cleanup.bat', None)
    build.classify('cleanup.command', None)

    build.documentation('*.html')
    build.documentation('*.txt')
    #build.documentation('*.pdf')

    #if config.???
