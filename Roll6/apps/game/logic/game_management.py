import random
from Roll6.apps.game.logic.parsing import string_to_list
from django.db.models import Q
from django.core import exceptions
from Roll6.apps.game.models import *


def get_moves(character_type=""):
    return Moves.objects.filter(Q(char_class__char_class=character_type)) if character_type else Moves.objects.get()


def get_move(move_ID = None):
    return Moves.objects.get(move_ID=move_ID)

def get_char_classes_list():
    list = []
    obj = CharacterClasses.objects.all()
    for char in obj:
        list.append(char.char_class)
    return list

def get_all_gear():
    return Gear.objects.get()


def get_gear(character_type=""):
    return AssignedGear.objects.filter(Q(char_class__char_class=character_type)) if character_type else AssignedGear.objects.get()


def get_weapon(weapon_ID = None):
    return Gear.objects.get(gear_ID=weapon_ID)


def get_gear_info(gear_id=""):
    return Gear.objects.filter(Q(gear_ID=gear_id) if gear_id else Gear.objects.get())


def get_ratings(character_type=""):
    return Ratings.objects.filter(Q(char_class__char_class=character_type)) if character_type else Ratings.objects.get()


def get_improvements(character_type=""):
    return Improvements.objects.filter(Q(char_class__char_class=character_type)) if character_type else Improvements.objects.get()


def get_improvement(improvement_ID=None):
    return Improvements.objects.get(improvement_ID=improvement_ID)


def get_adv_improvements(character_type=""):
    return AdvImprovements.objects.filter(Q(char_class__char_class=character_type)) if character_type else AdvImprovements.objects.get()


def get_adv_improvement(improvement_ID=None):
    return AdvImprovements.objects.get(improvement_ID=improvement_ID)


def get_ratings_values(hunter, rating_id):
    return_list = []
    all_ratings = get_ratings(hunter)
    for rating in all_ratings:
        if (int(rating.rating_ID) == int(rating_id)):
            return_list.append(rating.charm_modifier)
            return_list.append(rating.cool_modifier)
            return_list.append(rating.sharp_modifier)
            return_list.append(rating.tough_modifier)
            return_list.append(rating.weird_modifier)

    return return_list


def get_keeper_games(user_id=""):
    return Game.objects.filter(Q(user_ID=user_id)) if user_id else Game.objects.filter(Q())


def get_hunter_info(game_id="",hunter= ""):
    try:
        return ActiveGames.objects.get(Q(game_ID=game_id,char_class__char_class=hunter))
    except exceptions.ObjectDoesNotExist:
        return None

def generate_hunter_data(game_ID="", hunter=""):
    obj = ActiveGames.objects.get(Q(game_ID__game_ID=game_ID, char_class__char_class=hunter))
    moves = string_to_list(obj.move_list)
    weapons = string_to_list(obj.weapon_list)
    improvements = string_to_list(obj.improvements_list)
    advimprovements = string_to_list(obj.advImprovements_list)

    moveobjs = []
    for move in moves:
        moveobjs.append(get_move(move))

    weaponobjs = []
    for weapon in weapons:
        weaponobjs.append(get_weapon(weapon))

    improvementobjs = []
    if improvements is not False:
        for improvement in improvements:
            improvementobjs.append(get_improvement(improvement))
    else:
        improvementobjs = False

    advimprovementobjs = []
    if advimprovements is not False:
        for advimprovement in advimprovements:
            advimprovementobjs.append(advimprovement)
    else:
        advimprovementobjs = False

    return moveobjs, weaponobjs, improvementobjs, advimprovementobjs


def get_hunter_games(user_id=""):
    return LinkHunter.objects.filter(Q(user_ID=user_id)) if user_id else Game.objects.filter(Q())


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

    Game.objects.create(game_ID=potential_id, game_name=game_name, user_ID=keeper_id)
    return potential_id


def get_class_id(charclassstring):
    return CharacterClasses.objects.get(char_class=charclassstring).id

def check_character(charclass, GameID):
    #if there is a character already it returns true
    if ActiveGames.objects.filter(Q(game_ID=GameID,char_class_id=get_class_id(charclass))):
        return True
    else:
        return False


def create_character(GameID,charclass,charname,description,charm,cool,sharp,tough,weird,luck,harm,experience,move_list,weapon_list,history_list,improvements_list,advImprovements_list,char_specific):
    if ActiveGames.objects.filter(Q(game_ID=GameID,char_class_id=get_class_id(charclass))):
        return False
    else:
        ActiveGames.objects.create(game_ID_id=GameID,char_class_id=get_class_id(charclass),char_name=charname,description=description,charm=charm,cool=cool,sharp=sharp,tough=tough,weird=weird,luck=luck,harm=harm,experience=experience,move_list=move_list,weapon_list=weapon_list,history_list=history_list,improvements_list=improvements_list,advImprovements_list=advImprovements_list,char_specific=char_specific)
        return True


def update_character(GameID,charclass,description,charm,cool,sharp,tough,weird,luck,harm,experience,move_list,weapon_list,history_list,improvements_list,advImprovements_list,char_specific):
    obj = ActiveGames.objects.get(Q(game_ID=GameID,char_class_id=get_class_id(charclass)))
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
