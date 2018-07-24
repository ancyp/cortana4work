from parsing_service.skill_hr import skill_hr_root
def resolve_intent(intent):
    # todo: should this pass a function that will be used or a URL
    intents = {
        'add-time-off': skill_hr_root,
        'get-time-off': skill_hr_root,
    }
    
    return intents.get(intent['intent'])
