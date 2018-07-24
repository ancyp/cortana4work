from skills.skill_hr import skill_hr_root
from flask import render_template


def no_intent_found(intent):
    return render_template("no_intent.html")


def resolve_intent(intent):
    # todo: should this pass a function that will be used or a URL
    intents = {
        'add-time-off': skill_hr_root,
        'get-time-off': skill_hr_root,
    }

    if intent['intent'] not in intents.keys():
        return no_intent_found
    return intents.get(intent['intent'])
