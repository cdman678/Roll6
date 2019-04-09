from django.shortcuts import *
from django.template.loader import get_template

from Roll6.apps.game.logic.game_management import *
from Roll6.apps.game.logic.parsing import parse_push


# Create your views here.

def index(request):
    t = get_template('game/game.html')
    return HttpResponse(t.render())

def choosecharacter(request):
    temp = get_template('game/choosecharacter.html')
    return HttpResponse(temp.render())

def fillsheet(request, hunter):
    if request.method == 'POST':
        parsed_list = parse_push(request.POST)
        return HttpResponse("done")
    else:
        move_list = get_moves(hunter)
        gear_list = get_gear(hunter)
        rating_list = get_ratings(hunter)

        return render(request, 'game/fillsheet.html', {'type': hunter,
                                                       'move_list': move_list,
                                                       'gear_list': gear_list,
                                                       'rating_list': rating_list})