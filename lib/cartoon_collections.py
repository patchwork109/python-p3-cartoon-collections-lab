def roll_call_dwarves(names_list):
    # Solution 1
    # for x in range(len(names_list)):
    #     line = str(x + 1) + ". " + names_list[x]
    #     print(line)

    # Solution 2
    # the_count = 1
    # for one_name in names_list:
    #     print(f"{the_count}. {one_name}")
    #     the_count += 1

    # Solution 3
    for the_count, one_name in enumerate(names_list, start=1):
        print(f"{the_count}. {one_name}")




def summon_captain_planet(planeteer_calls):
    call_with_exclamation = [(call.capitalize() + "!") for call in planeteer_calls]
    print(call_with_exclamation)
    return call_with_exclamation

    # for the_word in planeteer_calls:
    #     call_with_exclamation = f"{the_word.capitalize()}!"
    # return call_with_exclamation




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
    
