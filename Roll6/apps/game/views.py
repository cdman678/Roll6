from django.shortcuts import *
from django.template.loader import get_template

from Roll6.apps.game.logic.game_management import *


# Create your views here.

def index(request):
    t = get_template('game/game.html')
    return HttpResponse(t.render())

def choosecharacter(request):
    temp = get_template('game/choosecharacter.html')
    return HttpResponse(temp.render())

def fillsheet(request, hunter):
    if request.method == 'POST':
        print (request.POST)
        return HttpResponse("Hello")
    else:
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