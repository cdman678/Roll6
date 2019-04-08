from django.db.models import Q
import random

from Roll6.apps.game.models import *


def get_moves(character_type):
    return Moves.objects.filter(Q(char_class__char_class=character_type))


def generate_game_id():
    alpha = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
    num = '01234567890'
    generated = ''
    for i in range(0,4):
        generated = generated + random.choice([random.choice(num),random.choice(alpha)])
    return generated


def create_new_game(game_name, keeper_name):
    potential_id = generate_game_id()
    while potential_id in Game.objects.filter(Q(game_ID=potential_id)):
        potential_id = generate_game_id()

    Game.objects.create(game_ID=potential_id,game_name=game_name, user_ID=keeper_name, keeper=True)
    return potential_id
