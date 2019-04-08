from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from django.template.loader import get_template

from Roll6.apps.game.logic.game_management import *


@login_required(login_url='index')
def maindash(request):
    hunter_games = get_hunter_games(request.user.id)
    keeper_games = get_keeper_games(request.user.id)
    return render(request, 'dashboard/maindash.html', {'hunter_games': hunter_games, 'keeper_games': keeper_games})


@login_required(login_url='index')
def motwfaq(request):
    temp = get_template('dashboard/motwfaq.html')
    return HttpResponse(temp.render())


@login_required(login_url='index')
def roll6faq(request):
    temp = get_template('dashboard/roll6faq.html')
    return HttpResponse(temp.render())


def wifu(request):
    temp = get_template('dashboard/wifu.html')
    return HttpResponse(temp.render())
