import random


def dice_roll(dice_count, die_sides):
    total_roll = 0
    for i in range(0, dice_count):
        total_roll += random.randint(1, die_sides)
    return total_roll
