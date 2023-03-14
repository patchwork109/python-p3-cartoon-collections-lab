def roll_call_dwarves(names_list):
    for x in range(len(names_list)):
        line = str(x + 1) + ". " + names_list[x]
        print(line)

def summon_captain_planet(planeteer_calls):
    call_with_exclamation = [(call.capitalize() + "!") for call in planeteer_calls]
    print(call_with_exclamation)
    return call_with_exclamation


def long_planeteer_calls(planeteer_calls):
    for x in range(len(planeteer_calls)):
        if len(planeteer_calls[x]) > 4:
            return True
    return False


def find_the_cheese(list_of_strings):
    if "cheddar" in list_of_strings:
        return "cheddar"
    elif "gouda" in list_of_strings:
        return "gouda"
    elif "camembert" in list_of_strings:
        return "camembert"
    else:
        return None
    
