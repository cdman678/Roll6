from Roll6.apps.game.logic.game_management import fix_id

def string_to_list(string):
    """
    :param string: The string to split, should be a comma separated list
    :return: the list of strings
    """
    out = []
    if isinstance(string, str):
        out = string.split(',')
    return out

# Will need changes as create character becomes developed - Caleb's work ATM
def parse_push(push_request):
    """
    :param push_request: *THIS WILL CHANGE* : name, moves, gear, ratings
    :return: gameID, characterClass, name, description, charm, cool, sharp, tough, weird, luck, harm,
             experience, moveList, weaponList, history, improvement, advImprovment, characterSpecific
    """

    #Remove the token from the list
    new_push_request = removekey(push_request,"csrfmiddlewaretoken")

    username = ""
    moves = []
    gear = []
    rating = ""
    multiple_ratings = False

    #  This for loop seperates push results into
    for item in new_push_request:
        # Finding user name
        if item == 'username':
            username = new_push_request[item][0]
        # Finding selected moves
        elif item[0] == 'm':
            move_id = fix_id(item)
            moves.append(move_id)
        # Finding selected gear
        elif item[0] == 'g':
            gear_id = fix_id(item)
            gear.append(gear_id)
        # Finding selected ratings
        elif item[0] == 'r':
            # Making sure this is the first ratings that was selected
            if len(rating) == 0:
                # Making sure I don't read off the list
                rating_temp = fix_id(item)
                if len(rating_temp) == 1:
                    rating = rating_temp[0]
            # This triggers if the user entered more than one ratings and will revert ratings to
            # an empty string which will be caught during varification
            else:
                multiple_ratings = True

    if multiple_ratings == True:
        del rating
        rating = ""

    print(username)
    print(moves)
    print(gear)
    print(rating)


#Used for removing items in a dictionary
def removekey(dictionary, key):
    r = dict(dictionary)
    del r[key]
    return r