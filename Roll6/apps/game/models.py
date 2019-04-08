from django.db import models


# Create your models here.
class Game(models.Model):
    game_ID = models.CharField(max_length=4,primary_key=True)
    game_name = models.CharField(max_length=30)
    keeper = models.BooleanField
    pub_date = models.DateTimeField('date published')
    last_run_date = models.DateTimeField('date last run')


class ActiveGames(models.Model):
    game_ID = models.CharField(max_length=4,primary_key=True)
    char_class = models.CharField(max_length=20)
    char_name = models.CharField(max_length= 20)
    description = models.CharField(max_length=99999)
    charm = models.IntegerField()
    cool = models.IntegerField()
    sharp = models.IntegerField()
    tough = models.IntegerField()
    weird = models.IntegerField()
    luck = models.IntegerField()
    harm = models.IntegerField()
    experience = models.IntegerField()

    move_list = models.CharField(max_length=100)
    weapon_list = models.CharField(max_length=100)
    improvements_list = models.CharField(max_length=100)
    advImprovements_list = models.CharField(max_length=100)

    class Meta:
        unique_together = (('game_ID','char_class'),)


class Moves(models.Model):
    move_ID = models.IntegerField(primary_key=True)
    char_type = models.CharField(max_length=20)
    move_name = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    default = models.BooleanField()
    mechanics = models.CharField(max_length=100)

    class Meta:
        unique_together = (('move_ID','char_type'),)


class Gear(models.Model):
    gear_ID = models.IntegerField(primary_key=True)
    weapon_name = models.CharField(max_length=20)
    damage = models.IntegerField()
    mechanic = models.CharField(max_length=100)

    class Meta:
        unique_together = (('gear_ID','weapon_name'),)


class AssignedGear(models.Model):
    char_class = models.CharField(max_length=20,primary_key=True)
    gear_ID = models.IntegerField()


class Ratings(models.Model):
    rating_ID = models.IntegerField(primary_key=True)
    char_class = models.CharField(max_length=20)
    charm_modifier = models.IntegerField()
    cool_modifier = models.IntegerField()
    sharp_modifier = models.IntegerField()
    tough_modifier = models.IntegerField()
    weird_modifier = models.IntegerField()

    class Meta:
        unique_together = (('rating_ID','char_class'),)


class Improvements(models.Model):
    improvement_ID = models.IntegerField(primary_key=True)
    char_class = models.CharField(max_length=20)
    text_improvement = models.CharField(max_length=20)
    charm_modifier = models.IntegerField()
    cool_modifier = models.IntegerField()
    sharp_modifier = models.IntegerField()
    tough_modifier = models.IntegerField()
    weird_modifier = models.IntegerField()

    class Meta:
        unique_together = (('improvement_ID', 'char_class'),)


class AdvImprovements(models.Model):
    improvement_ID = models.IntegerField(primary_key=True)
    char_class = models.CharField(max_length=20)
    improvement = models.CharField(max_length=100)

    class Meta:
        unique_together = (('improvement_ID','char_class'),)


class Fate(models.Model):
    fate_ID = models.IntegerField(primary_key=True)
    heroic = models.BooleanField()
    doom = models.BooleanField()
    fate_tag = models.CharField(max_length=20)


class Heat(models.Model):
    heat_ID = models.IntegerField(primary_key=True)
    heat_description = models.CharField(max_length=1000)


class Underworld(models.Model):
    underworld_ID = models.IntegerField(primary_key=True)
    underworld_description = models.CharField(max_length=1000)


class Haven(models.Model):
    haven_ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)


class Sect(models.Model):
    sect_ID = models.IntegerField(primary_key=True)
    good = models.BooleanField()
    bad = models.BooleanField()
    sect_tag = models.CharField(max_length=100)


class Agency(models.Model):
    agency_ID = models.IntegerField(primary_key=True)
    resource = models.BooleanField()
    red_tape = models.BooleanField()
    option = models.CharField(max_length=20)


class Spells(models.Model):
    spell_ID = models.IntegerField(primary_key=True)
    base = models.BooleanField()
    effect = models.BooleanField()
    spell_name = models.CharField(max_length=20)
    spell_description = models.CharField(max_length=1000)


class DarkSide(models.Model):
    tag_ID = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=20)


class Lost(models.Model):
    id = models.IntegerField(primary_key=True)
    who = models.BooleanField()
    what = models.BooleanField()
    description = models.CharField(max_length=1000)

