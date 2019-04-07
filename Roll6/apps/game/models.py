from django.db import models


# Create your models here.
class Game(models.Model):
    access_key = models.CharField(max_length=4)
    game_name = models.CharField(max_length=30)
    keeper = models.BooleanField
    pub_date = models.DateTimeField('date published')
    last_run_date = models.DateTimeField('date last run')


class ActiveGames(models.Model):
    gameID = models.CharField(max_length=4)
    charclass = models.CharField(max_length=20)
    charName = models.CharField(max_length= 20)
    description = models.CharField(max_length=99999)
    charm = models.IntegerField()
    cool = models.IntegerField()
    sharp = models.IntegerField()
    tough = models.IntegerField()
    weird = models.IntegerField()
    luck = models.IntegerField()
    harm = models.IntegerField()
    experience = models.IntegerField()

    moveList = models.CharField(max_length=100)
    weaponList = models.CharField(max_length=100)
    improvementsList = models.CharField(max_length=100)
    advImprovementsList = models.CharField(max_length=100)


class Moves(models.Model):
    moveid = models.IntegerField()
    charType= models.CharField(max_length=20)
    movename = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    default = models.BooleanField()
    mechanics = models.CharField(max_length=100)


class Gear(models.Model):
    gearID = models.IntegerField()
    weaponname = models.CharField(max_length=20)
    damage = models.IntegerField()
    mechanic = models.CharField(max_length=100)


class AssignedGear(models.Model):
    charclass = models.CharField(max_length=20)
    gearID = models.IntegerField()


class Ratings(models.Model):
    ratingID = models.IntegerField()
    charclass = models.CharField(max_length=20)
    charmModifier = models.IntegerField()
    coolModifier = models.IntegerField()
    sharpModifier = models.IntegerField()
    toughModifier = models.IntegerField()
    weirdModifier = models.IntegerField()


class Improvements(models.Model):
    improvementID = models.IntegerField()
    charclass = models.CharField(max_length=20)
    textimprovement = models.CharField(max_length=20)
    charmModifier = models.IntegerField()
    coolModifier = models.IntegerField()
    sharpModifier = models.IntegerField()
    toughModifier = models.IntegerField()
    weirdModifier = models.IntegerField()


class AdvImprovements:
    improvementID = models.IntegerField()
    charclass = models.CharField(max_length=20)
    improvement = models.CharField(max_length=100)


class Fate:
    fateID = models.IntegerField()
    heroic = models.BooleanField()
    doom = models.BooleanField()
    fatetag = models.CharField(max_length=20)


class Heat:
    heatID = models.IntegerField()
    heatDescription = models.CharField(max_length=1000)


class Underworld:
    underworldID = models.IntegerField()
    underworldDescription = models.CharField(max_length=1000)


class Haven:
    havenID = models.IntegerField()
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=1000)


class Sect:
    sectID = models.IntegerField()
    good = models.BooleanField()
    bad = models.BooleanField()
    secttag = models.CharField(max_length=100)


class Agency:
    agencyID = models.IntegerField()
    resource = models.BooleanField()
    redtape = models.BooleanField()
    option = models.CharField(max_length=20)


class Spells:
    spellID = models.IntegerField()
    base = models.BooleanField()
    effect = models.BooleanField()
    spellname = models.CharField(max_length=20)
    spelldescription = models.CharField(max_length=1000)


class DarkSide:
    tagID = models.IntegerField()
    tag = models.CharField(max_length=20)


class Lost:
    id = models.IntegerField()
    who = models.BooleanField()
    what = models.BooleanField()
    description = models.CharField(max_length=1000)

