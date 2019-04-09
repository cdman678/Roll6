#this code will need to be changed as the pasrsed list changes
def verify_new_character(hunter, parsed_list):
    name = parsed_list[0]
    moves = parsed_list[1]
    gear = parsed_list[2]
    ratings = parsed_list[3]

    #The list that will display all invalid inpurs on the character creation screen
    issues = []

    #name check
    if name == "":
        issues.append("Please enter a name")

    #moves check
    if not move_check(hunter, len(moves)):
        issues.append("Invalid number of moves")

    #gear check
    if not gear_check(hunter, len(gear)):
        issues.append("Invalid number of gear choices selected")

    if ratings == "":
        issues.append("Please select only 1 rating")

    return issues


def move_check(hunter,length):
    if hunter in "chosen":
        return (length == 1)
    elif hunter in "crooked-expert-monstrous-wronged":
        return (length == 2)
    elif hunter in "divine-flake-initiate-mundane-spell-slinger-spooky":
        return (length == 3)
    elif hunter in "professional":
        return (length == 4)


def gear_check(hunter,length):
    #Current problem classes - always pass true until we fix this
    if hunter in "chosen-flake-initiate-professional-wronged":
        return True
    elif hunter in "divine-monstrous-spell-slinger":
        return (0 < length <= 1)
    elif hunter in "mundane-spooky":
        return (0 < length <= 2)
    elif hunter in "crooked-expert":
        return (0 < length <= 3)








