from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


# Create your views here.


def index(request):
    t = get_template('game/game.html')
    return HttpResponse(t.render())

def choosecharacter(request):
    temp = get_template('game/choosecharacter.html')
    return HttpResponse(temp.render())

def fillsheet(request, hunter):
    return render(request, "game/fillsheet.html", {'type': hunter})
