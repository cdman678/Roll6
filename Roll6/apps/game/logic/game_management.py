from django.db.models import Q
import random

from Roll6.apps.game.models import *


def get_moves(character_type=""):
    return Moves.objects.filter(Q(char_class__char_class=character_type)) if character_type else Moves.objects.get()


def get_all_gear():
    return Gear.objects.get()


def get_assigned_gear(character_type=""):
    return AssignedGear.objects.filter(Q(char_class__char_class=character_type)) if character_type else AssignedGear.objects.get()


def get_improvements(character_type=""):
    return Improvements.objects.filter(Q(char_class__char_class=character_type)) if character_type else Improvements.objects.get()


def get_adv_improvements(character_type=""):
    return AdvImprovements.objects.filter(Q(char_class__char_class=character_type)) if character_type else AdvImprovements.objects.get()


def get_ratings(character_type=""):
    return Ratings.objects.filter(Q(char_class__char_class=character_type)) if character_type else Ratings.objects.get()


def get_keeper_games(user_id=""):
    return Game.objects.filter(Q(user_ID=user_id, keeper=True)) if user_id else Game.objects.filter(Q(keeper=True))


def get_hunter_games(user_id=""):
    return Game.objects.filter(Q(user_ID=user_id, keeper=False)) if user_id else Game.objects.filter(Q(keeper=False))


def generate_game_id():
    alpha = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
    num = '1234567890'
    generated = ''
    for i in range(0,4):
        generated = generated + random.choice(num+alpha)
    return generated


def create_new_game(game_name, keeper_name):
    potential_id = generate_game_id()
    while potential_id in Game.objects.filter(Q(game_ID=potential_id)):
        potential_id = generate_game_id()

    Game.objects.create(game_ID=potential_id,game_name=game_name, user_ID=keeper_name, keeper=True)
    return potential_id

