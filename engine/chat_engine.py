from engine.response_rules import rules

def get_chat (user):
    if user in rules.keys():
        return rules.get(user)
    else:
        return "sorry i cant understand !"
        

