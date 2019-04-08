from django.db import models


# Create your models here.
class Game(models.Model):
    gameID = models.CharField(max_length=4,primary_key=True)
    game_name = models.CharField(max_length=30)
    keeper = models.BooleanField
    pub_date = models.DateTimeField('date published')
    last_run_date = models.DateTimeField('date last run')


class ActiveGames(models.Model):
    gameID = models.CharField(max_length=4,primary_key=True)
    charClass = models.CharField(max_length=20)
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

    class Meta:
        unique_together = (('gameID','charClass'),)


class Moves(models.Model):
    moveid = models.IntegerField(primary_key=True)
    charType= models.CharField(max_length=20)
    movename = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    default = models.BooleanField()
    mechanics = models.CharField(max_length=100)

    class Meta:
        unique_together = (('moveid','charType'),)


class Gear(models.Model):
    gearID = models.IntegerField(primary_key=True)
    weaponName = models.CharField(max_length=20)
    damage = models.IntegerField()
    mechanic = models.CharField(max_length=100)

    class Meta:
        unique_together = (('gearID','weaponName'),)


class AssignedGear(models.Model):
    charclass = models.CharField(max_length=20,primary_key=True)
    gearID = models.IntegerField()


class Ratings(models.Model):
    ratingID = models.IntegerField(primary_key=True)
    charClass = models.CharField(max_length=20)
    charmModifier = models.IntegerField()
    coolModifier = models.IntegerField()
    sharpModifier = models.IntegerField()
    toughModifier = models.IntegerField()
    weirdModifier = models.IntegerField()

    class Meta:
        unique_together = (('ratingID','charClass'),)


class Improvements(models.Model):
    improvementID = models.IntegerField(primary_key=True)
    charClass = models.CharField(max_length=20)
    textimprovement = models.CharField(max_length=20)
    charmModifier = models.IntegerField()
    coolModifier = models.IntegerField()
    sharpModifier = models.IntegerField()
    toughModifier = models.IntegerField()
    weirdModifier = models.IntegerField()

    class Meta:
        unique_together = (('improvementID', 'charClass'),)


class AdvImprovements(models.Model):
    improvementID = models.IntegerField(primary_key=True)
    charClass = models.CharField(max_length=20)
    improvement = models.CharField(max_length=100)

    class Meta:
        unique_together = (('improvementID','charClass'),)


class Fate(models.Model):
    fateID = models.IntegerField(primary_key=True)
    heroic = models.BooleanField()
    doom = models.BooleanField()
    fatetag = models.CharField(max_length=20)


class Heat(models.Model):
    heatID = models.IntegerField(primary_key=True)
    heatDescription = models.CharField(max_length=1000)


class Underworld(models.Model):
    underworldID = models.IntegerField(primary_key=True)
    underworldDescription = models.CharField(max_length=1000)


class Haven(models.Model):
    havenID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=1000)


class Sect(models.Model):
    sectID = models.IntegerField(primary_key=True)
    good = models.BooleanField()
    bad = models.BooleanField()
    secttag = models.CharField(max_length=100)


class Agency(models.Model):
    agencyID = models.IntegerField(primary_key=True)
    resource = models.BooleanField()
    redtape = models.BooleanField()
    option = models.CharField(max_length=20)


class Spells(models.Model):
    spellID = models.IntegerField(primary_key=True)
    base = models.BooleanField()
    effect = models.BooleanField()
    spellname = models.CharField(max_length=20)
    spelldescription = models.CharField(max_length=1000)


class DarkSide(models.Model):
    tagID = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=20)


class Lost(models.Model):
    id = models.IntegerField(primary_key=True)
    who = models.BooleanField()
    what = models.BooleanField()
    description = models.CharField(max_length=1000)

