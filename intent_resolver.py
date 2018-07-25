from skills.skill_hr import skill_hr_root
from skills.skill_addevent import skill_addevent_root
from flask import render_template, Blueprint

intent_resolver = Blueprint('intent_resolver',__name__)


def no_intent_found(intent):
    return render_template("no_intent.html")


@intent_resolver.route("/resolve-intent")
def resolve_intent(intent):
    intents = {
        'add-time-off': skill_hr_root,
        'get-time-off': skill_hr_root,
        'add-task': skill_addevent_root
    }

    if intent['intent'] not in intents.keys():
        return no_intent_found
    return intents.get(intent['intent'])
