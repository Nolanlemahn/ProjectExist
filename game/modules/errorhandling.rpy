init python:
    # This function is responsible for taking a traceback, and converting
    # it to a string that can be shown with text.
    def format_traceback(s):
        import re

        lines = [ i.replace("{", "{{") for i in s.split("\n") ]

        rv = [ "{b}" + lines[0] + "{/b}" ]

        for i in lines[1:]:
            i = re.sub(r'(File "(.*)", line (\d+))', r'{a=edit:\3:\2}\1{/a}', i)
            rv.append(i)

        return "\n".join(rv)

    class __XScrollValue(BarValue):
        def __init__(self, viewport):
            self.viewport = viewport

        def get_adjustment(self):
            w = renpy.get_widget(None, self.viewport)
            if not isinstance(w, Viewport):
                raise Exception("The displayable with id %r is not declared, or not a viewport." % self.viewport)

            return w.xadjustment

        def get_style(self):
            return "scrollbar", "vscrollbar"

    class __YScrollValue(BarValue):
        def __init__(self, viewport):
            self.viewport = viewport

        def get_adjustment(self):
            w = renpy.get_widget(None, self.viewport)
            if not isinstance(w, Viewport):
                raise Exception("The displayable with id %r is not declared, or not a viewport." % self.viewport)

            return w.yadjustment

        def get_style(self):
            return "scrollbar", "vscrollbar"

    class _EditFile(Action):
        def __init__(self, filename, line=1):
            self.filename = filename
            self.line = line

        def __call__(self):
            try:
                renpy.launch_editor([ self.filename ], self.line, transient=1)
            except:
                pass

    class __ErrorQuit(Action):
        """
        An action that quits with an error status.
        """

        def __call__(self):
            renpy.quit(status=1)

    # The transform used for errors. ATL isn't ready yet.
    def exception_transform_func(state, st, at):
        done = min(st / .1, 1.0)
        state.zoom = .5 + .5 * done
        state.alpha = done
        state.xalign = 0.5
        state.yalign = 0.5

        if done < 1.0:
            return 0
        else:
            return None

    exception_trans = Transform(function=exception_transform_func, style='_default')

init 1:
# The screen that is used for error handling.
    screen _exception:
        modal True
        zorder 1090

        default tt = Tooltip("")
        default fmt_short = format_traceback(short)
        default fmt_full = format_traceback(full)

        add Solid("#000")

        frame:
            style_group ""
            xfill True

            at exception_trans

            has side "t c r b"

            vbox:
                label _("An exception has occurred.")

            viewport:
                id "viewport"
                child_size (4000, None)
                mousewheel True

                has vbox

                text fmt_short substitute False
                text fmt_full substitute False

            bar:
                style "_vscrollbar"
                value __YScrollValue("viewport")

            vbox:

                bar:
                    style "_scrollbar"
                    value __XScrollValue("viewport")

                hbox:
                    box_wrap True

                    if rollback_action:
                        textbutton _("Rollback"):
                            action renpy.exports.rollback(force=True)
                            hovered tt.action(_("Attempts a roll back to a prior time, allowing you to save or choose a different choice."))

                    if ignore_action:
                        textbutton _("Ignore"):
                            action ignore_action
                            hovered tt.action(_("Ignores the exception, allowing you to continue. This often leads to additional errors."))

                    if config.developer:
                        textbutton _("Reload"):
                            action reload_action
                            hovered tt.action(_("Reloads the game from disk, saving and restoring game state if possible."))

                    textbutton _("Open Traceback"):
                        action _EditFile(traceback_fn)
                        hovered tt.action(_("Opens the traceback.txt file in a text editor."))

                    null width 30

                    textbutton _("Report This"):
                        action Help("game/modules/report.html")
                        hovered tt.action(_("Send a report to the developers."))

                    textbutton _("Quit"):
                        action __ErrorQuit()
                        hovered tt.action(_("Quits the game."))

                # Tooltip.
                text tt.value size 12

        if config.developer and reload_action:
            key "R" action reload_action