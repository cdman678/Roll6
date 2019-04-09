from django.shortcuts import *
from django.template.loader import get_template

from Roll6.apps.game.logic.character_verification import verify_new_character
from Roll6.apps.game.logic.game_management import *
from Roll6.apps.game.logic.parsing import parse_push


# Create your views here.

def index(request):
    t = get_template('game/game.html')
    create_character('zzzz',"mundane","Jimmy","I have stuff here",0,0,0,0,0,0,0,0,"","","","","","")
    update_character('zzzz',"mundane","new stuff",0,0,0,0,0,0,0,0,"1,2,4,5","","","","","")
    return HttpResponse(t.render())


def join_game(request):
    if request.method == 'POST':
        gameID = request.POST["gameid"]
        temp_string = '/game/'+gameID+'/choosecharacter/'
        return redirect(temp_string)
    return render(request,'game/joingame.html')


def choosecharacter(request, gameid):
    return render(request, 'game/choosecharacter.html', {'gameID': gameid})


def fillsheet(request, gameid, hunter):
    if request.method == 'POST':
        parsed_list = parse_push(request.POST)
        logic_result = verify_new_character(hunter, parsed_list)
        if len(logic_result) == 0:
            return HttpResponse("no errors")
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
        gameid = gameid
        move_list = get_moves(hunter)
        gear_list = get_gear(hunter)
        rating_list = get_ratings(hunter)

        return render(request, 'game/fillsheet.html', {'type': hunter,
                                                       'move_list': move_list,
                                                       'gear_list': gear_list,
                                                       'rating_list': rating_list})