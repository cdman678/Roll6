from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.


def index(request):
    t = get_template('game/game.html')
    return HttpResponse(t.render())
