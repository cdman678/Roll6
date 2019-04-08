from django.db.models import Q

from Roll6.apps.game.models import *


def get_moves(character_type):
    return Moves.objects.filter(Q(char_class__char_class=character_type))


def create_new_game(game_name):
    return
