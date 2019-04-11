import random


def dice_roll(dice_count, die_sides):
    roll = []
    for i in range(0, dice_count):
         roll.append(random.randint(1, die_sides))
    return roll
