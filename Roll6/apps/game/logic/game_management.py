from Roll6.apps.game.models import *
from django.db.models import Q


def get_moves(character_type):
    return Moves.objects.filter(Q(char_type=character_type))