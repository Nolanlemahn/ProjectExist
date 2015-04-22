init -3 python:
    def watch(expression, style='default', func_name="default_renpy_watch", **properties):
        """
        :doc: debug

        This watches the given python expression, by displaying it in the
        upper-left corner of the screen (although position properties
        can change that). The expression should always be
        defined, never throwing an exception.

        A watch will not persist through a save or restart.

        `func_name`
            A string that can be used to give the watch function an internal name.
            This makes the function "stoppable" in the unwatch function.
        """

        def overlay_func():
            overlay_func.watch_name = func_name

            renpy.ui.text(unicode(renpy.python.py_eval(expression)),
                          style=style, **properties)

        renpy.config.overlay_functions.append(overlay_func)

    def unwatch(all=False, func_name=None):
        """
        :doc: debug

        This stops renpy.watch calls by checking config.overlay_functions for 
        functions with the attribute `watch_name`.

        `all`
            If True, removes multiple functions in renpy.overlay_functions that 
            have the `watch_name` attribute.

        `func_name`
            If not None (and `all` is False), a function with the corresponding
            `watch_name` is removed. If `all` is True instead, every function
            with the corresponding `watch_name` is removed.
        """

        for f in renpy.config.overlay_functions:
            if hasattr(f, "watch_name"):
                if all == False:
                    # [False, None] case (technically invalid, since we aren't told 
                    # to remove anything). Just return.
                    if func_name is None:
                        return

                    # [False, not None] case. Remove the first valid function we 
                    # see, then return.
                    else:
                        if f.watch_name == func_name:
                            renpy.config.overlay_functions.remove(f)
                            return
                else:
                    # [True, None] case. Remove everything.
                    if func_name is None:
                        renpy.config.overlay_functions.remove(f)
                        unwatch(all, func_name)

                    # [True, not None] case. Remove every valid function we see.
                    else:
                        if f.watch_name == func_name:
                            renpy.config.overlay_functions.remove(f)
                            unwatch(all, func_name)