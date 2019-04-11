from django.shortcuts import *
from django.template.loader import get_template
import math

from Roll6.apps.game.logic.character_verification import verify_new_character
from Roll6.apps.game.logic.game_management import *
from Roll6.apps.game.logic.parsing import list_to_string
from Roll6.apps.game.logic.parsing import parse_push, string_to_list
from Roll6.apps.game.logic.parsing import removekey
from Roll6.apps.game.logic.dice import dice_roll


# Create your views here.

def dice(request):
    roll = dice_roll(2, 6)
    rollmath = roll[0] + roll[1]
    return render(request, 'game/dice.html', {'rollmath': rollmath, "rolls": roll})


def create_game(request):
    if request.method == 'POST':
        game_name = request.POST["gamename"]
        game_id = create_new_game(game_name, request.user.id)
        return render(request, 'game/creategame.html', {"gameID": game_id})
    return render(request, 'game/creategame.html')


def join_game(request):
    if request.method == 'POST':
        game_id = request.POST["gameid"]
        if get_game_by_id(game_id) is None:
            return render(request, 'game/joingame.html', {'invalidgame': True})
        temp_string = '/game/'+game_id+'/choosecharacter/'
        return redirect(temp_string)
    return render(request, 'game/joingame.html')


def choosecharacter(request, gameid):
    if request.method == 'POST':
        new_post = removekey(request.POST, "csrfmiddlewaretoken")
        hunter_type = ""
        for the_only in new_post:
            hunter_type = the_only
        #If character sheet exists
        if check_character(hunter_type, gameid) == True:

            temp = "/game/" + gameid + "/" + hunter_type
            return HttpResponseRedirect(temp)

        else:
            temp_string = '/game/'+str(gameid)+'/fill/'+hunter_type
            print(request.user)
            if request.user is not None and get_game_by_id(gameid).user_ID != request.user.id:
                make_hunter_link(request.user.id, gameid)
            return redirect(temp_string)

        # Create a new character
    return render(request, 'game/choosecharacter.html', {'gameID': gameid})


def game(request, gameid, hunter):
    keeper = get_game_by_id(gameid)
    if keeper.user_ID == request.user.id:
        if request.method == 'POST':
            button = request.POST['button']
            hunterobj = get_hunter_info(gameid, button)
            if hunterobj is None:
                return render(request, 'game/keeper.html', {'gameID': gameid, 'error': button})
            huntername = "The " + button[0:1].upper() + button[1:]
            level = math.floor(hunterobj.experience / 5)
            experience = hunterobj.experience % 5
            moves, weapons, improvements, advimprovements = generate_hunter_data(gameid, button)
            return render(request, 'game/keeper.html', {'gameID': gameid,
                                                        'huntername': huntername,
                                                        'hunter': hunterobj,
                                                        'level': level,
                                                        'experience': experience,
                                                        'moves': moves,
                                                        'weapons': weapons,
                                                        'improvements': improvements,
                                                        'advimprovements': advimprovements})
        return render(request, 'game/keeper.html', {'gameID': gameid})
    # You are a hunter
    else:
        if hunter in get_char_classes_list():
            hunterobj = get_hunter_info(gameid, hunter)
            if hunterobj is None:
                return HttpResponseRedirect("/game/" + gameid + '/choosecharacter')
            huntername = "The " + hunter[0:1].upper() + hunter[1:]
            level = math.floor(hunterobj.experience / 5)
            experience = hunterobj.experience % 5
            moves, weapons, improvements, advimprovements = generate_hunter_data(gameid, hunter)
            return render(request, 'game/hunter.html', {'gameID': gameid,
                                                        'huntername': huntername,
                                                        'hunter': hunterobj,
                                                        'level': level,
                                                        'experience': experience,
                                                        'moves': moves,
                                                        'weapons': weapons,
                                                        'improvements': improvements,
                                                        'advimprovements': advimprovements})
        else:
            # temp_string = "/game" + gameid + '/choosecharacter'
            return HttpResponseRedirect("/game/" + gameid + '/choosecharacter')


def update_sheet(request, gameid, hunter):
    hunterobj = get_hunter_info(gameid, hunter)
    if request.method == 'POST':
        parsed_list = parse_push(request.POST)
        charm = hunterobj.charm + int(request.POST['charm'])
        cool = hunterobj.cool + int(request.POST['cool'])
        sharp = hunterobj.sharp + int(request.POST['sharp'])
        tough = hunterobj.tough + int(request.POST['tough'])
        weird = hunterobj.weird + int(request.POST['weird'])
        luck = hunterobj.luck + int(request.POST['luck'])
        harm = hunterobj.harm + int(request.POST['harm'])
        experience = hunterobj.experience + int(request.POST['experience'])
        update_character(str(gameid),hunter,"",charm,cool,sharp,tough,weird,luck,harm,experience,list_to_string(parsed_list[1]),list_to_string(parsed_list[2]),"","","","")
        url = "/game/" + gameid + "/" + hunter
        return HttpResponseRedirect(url)
    else:
        move_list = get_moves(hunter)
        gear_list = get_gear(hunter)
        rating_list = get_ratings(hunter)
        moves, weapons, improvements, advimprovements = generate_hunter_data(gameid, hunter)
        huntername = "The " + hunter[0:1].upper() + hunter[1:]
        level = math.floor(hunterobj.experience / 5)
        return render(request, 'game/updatesheet.html', {'type': hunter,
                                                            'move_list': move_list,
                                                            'gear_list': gear_list,
                                                            'rating_list': rating_list,
                                                            'currentmoves': moves,
                                                            'currentweapons': weapons,
                                                            'huntername': huntername,
                                                            'hunterobj': hunterobj,
                                                            'level': level})


def fillsheet(request, gameid, hunter):
    if request.method == 'POST':
        parsed_list = parse_push(request.POST)
        logic_result = verify_new_character(hunter, parsed_list)
        if len(logic_result) == 0:
            rating_values = get_ratings_values(hunter, parsed_list[3])
            create_character(str(gameid),hunter,parsed_list[0],"",rating_values[0],rating_values[1],rating_values[2],rating_values[3],rating_values[4],7,0,0,list_to_string(parsed_list[1]),list_to_string(parsed_list[2]),"","","","")
            url = "/game/" + gameid + "/" + hunter
            return HttpResponseRedirect(url)
        else:
            move_list = get_moves(hunter)
            gear_list = get_gear(hunter)
            rating_list = get_ratings(hunter)
            return render(request, 'game/fillsheet.html', {'type': hunter,
                                                           'move_list': move_list,
                                                           'gear_list': gear_list,
                                                           'rating_list': rating_list,
                                                           'error_list': logic_result,
                                                           'invalid': True})

    else:
        move_list = get_moves(hunter)
        gear_list = get_gear(hunter)
        rating_list = get_ratings(hunter)

        return render(request, 'game/fillsheet.html', {'type': hunter,
                                                       'move_list': move_list,
                                                       'gear_list': gear_list,
                                                       'rating_list': rating_list})
