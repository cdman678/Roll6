from django.shortcuts import *
from django.template.loader import get_template

from Roll6.apps.game.logic.game_management import *


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
    print(gameid)
    temp = get_template('game/choosecharacter.html')
    return HttpResponse(temp.render())


def fillsheet(request, gameid, hunter):
    if request.method == 'POST':
        print (request.POST)
        return HttpResponse("Hello")
    else:
        gameid = gameid
        move_list = get_moves(hunter)
        avaliable_gear_list = get_gear(hunter)
        gear_temp = []
        for gear in avaliable_gear_list:
            temp = fix_id(str(gear.gear_ID))
            gear_temp.append(get_gear_info(int(temp)))
        rating_list = get_ratings(hunter)

        gear_info = []
        for queary in gear_temp:
            for gear in queary:
                gear_info.append(gear)


        return render(request, 'game/fillsheet.html', {'type': hunter,
                                                       'move_list': move_list,
                                                       'gear_info': gear_info,
                                                       'rating_list': rating_list})