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

    #returns lists of rows
    move_list = get_moves(hunter)

    return render(request, 'game/fillsheet.html', {'type': hunter, 'move_list': move_list})
