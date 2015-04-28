label triple_min(interval):
    $ minutes = minutes + interval
    "... "
    $ minutes = minutes + interval
    extend "... "
    $ minutes = minutes + interval
    extend "..."
    return

label addAnswer(new_answer):
    $ answers.append(new_answer)
    return

label removeAnswer(dead_answer):
    $ answers.remove(dead_answer)
    return

init -1 python:
    def addAnswer(new_answer):
        renpy.call("addAnswer", new_answer)
        return

    # Doesn't have a label version. Sorry!
    def hasAnswer(check_answer):
        return (check_answer in store.answers)

    def removeAnswer(dead_answer):
        renpy.call("removeAnswer", dead_answer)
        return

    def python_pass():
        return
        
    def triple_min(delta_minutes):
        renpy.call("triple_min", delta_minutes)
        return
        
    def init_points():
        temp_points = []
        for i in range(0, 10001):
            temp_points.append(0)
        return temp_points
        
    def sio_l(called_scene):
        renpy.scene()
        renpy.show("bg blackdrop")
        renpy.show("empty")
        renpy.with_statement(dissolve)
        renpy.scene()
        renpy.show(called_scene)
        renpy.show("empty")
        renpy.with_statement(dissolve)
        return
        
    def sio_s(called_scene):
        renpy.scene()
        renpy.show(called_scene)
        renpy.with_statement(dissolve)
    
    #question should be a string or None, *candidates is any number of strings as additional parameters
    #selected answer becomes red on-screen, returns integer (min=1) in accordance to which answer chosen
    #additionally requires following definition or similar (ctc need not be defined):
    # $ nvlcap = NVLCharacter(None, kind=nvl, ctc=anim.Blink("extra/arrow.png"))
    def nvlq(question, *candidates):
        full_answer = ""
        menu_answers = []
        string_answers = []
        num_answers = 0
        
        for answer in candidates:
            num_answers = num_answers + 1
            menu_answers.append(("> "+answer, num_answers))
            string_answers.append("> "+answer)
            
        if(question == None):
            result = nvl_menu(menu_answers)
        else:
            q = [(question, None)]
            q.extend(menu_answers)
            result = nvl_menu(q)
            
        string_answers[result-1] = "{color=#f00}" + string_answers[result-1] + "{/color}"
        for answer in string_answers:
            full_answer = full_answer + answer + "\n"
        full_answer = full_answer[:-1]
        
        if(question == None):
            renpy.say(nvlcap, full_answer + "{fast}")
        else:
            renpy.say(nvlcap, question + "\n" + full_answer + "{fast}")
        return result

    def nvlans(q_index, result):
        if(q_index == 0):
            q_answers = ["thought_heaven", "thought_hell", "thought_head_neither", "thought_head_empty"]
        else:
            return None
        return q_answers[result - 1]
