import random
import re

from django.db.models import Q

from Roll6.apps.game.models import *


def get_moves(character_type=""):
    return Moves.objects.filter(Q(char_class__char_class=character_type)) if character_type else Moves.objects.get()


def get_all_gear():
    return Gear.objects.get()


def get_gear(character_type=""):
    return AssignedGear.objects.filter(Q(char_class__char_class=character_type)) if character_type else AssignedGear.objects.get()


def get_gear_info(gear_id=""):
    return Gear.objects.filter(Q(gear_ID=gear_id) if gear_id else Gear.objects.get())


def get_ratings(character_type=""):
    return Ratings.objects.filter(Q(char_class__char_class=character_type)) if character_type else Ratings.objects.get()


def get_improvements(character_type=""):
    return Improvements.objects.filter(Q(char_class__char_class=character_type)) if character_type else Improvements.objects.get()


def get_adv_improvements(character_type=""):
    return AdvImprovements.objects.filter(Q(char_class__char_class=character_type)) if character_type else AdvImprovements.objects.get()


def fix_id(old_id):
    new_id = re.findall("\d[0-9]*", old_id)
    return new_id


def get_keeper_games(user_id=""):
    return Game.objects.filter(Q(user_ID=user_id, keeper=True)) if user_id else Game.objects.filter(Q(keeper=True))


def get_hunter_games(user_id=""):
    return Game.objects.filter(Q(user_ID=user_id, keeper=False)) if user_id else Game.objects.filter(Q(keeper=False))


def get_game_by_id(game_id=""):
    return Game.objects.filter(Q(game_ID=game_id)).first()


def generate_game_id():
    alpha = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
    num = '1234567890'
    generated = ''
    for i in range(0, 4):
        generated = generated + random.choice(num+alpha)
    return generated


def create_new_game(game_name, keeper_id):
    potential_id = generate_game_id()
    while potential_id in Game.objects.filter(Q(game_ID=potential_id)):
        potential_id = generate_game_id()

    Game.objects.create(game_ID=potential_id, game_name=game_name, user_ID=keeper_id, keeper=True)
    return potential_id


def get_class_id(charclassstring):
    return CharacterClasses.objects.get(char_class=charclassstring).id


def create_character(GameID,charclass,charname,description,charm,cool,sharp,tough,weird,luck,harm,experience,move_list,weapon_list,history_list,improvements_list,advImprovements_list,char_specific):
    if ActiveGames.objects.filter(Q(game_ID=GameID) and Q(char_class_id=get_class_id(charclass))):
        return False
    else:
        ActiveGames.objects.create(game_ID_id=GameID,char_class_id=get_class_id(charclass),char_name=charname,description=description,charm=charm,cool=cool,sharp=sharp,tough=tough,weird=weird,luck=luck,harm=harm,experience=experience,move_list=move_list,weapon_list=weapon_list,history_list=history_list,improvements_list=improvements_list,advImprovements_list=advImprovements_list,char_specific=char_specific)
        return True


def update_character(GameID,charclass,description,charm,cool,sharp,tough,weird,luck,harm,experience,move_list,weapon_list,history_list,improvements_list,advImprovements_list,char_specific):
    obj = ActiveGames.objects.get(Q(game_ID=GameID) and Q(char_class_id=get_class_id(charclass)))
    obj.description = description
    obj.charm = charm
    obj.cool = cool
    obj.sharp = sharp
    obj.tough = tough
    obj.weird = weird
    obj.luck = luck
    obj.harm = harm
    obj.experience = experience
    obj.move_list = move_list
    obj.weapon_list = weapon_list
    obj.history_list = history_list
    obj.improvements_list = improvements_list
    obj.advImprovements_list = advImprovements_list
    obj.char_specific = char_specific
    obj.save()
