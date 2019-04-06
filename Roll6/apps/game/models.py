from django.db import models


# Create your models here.
class Game(models.Model):
    access_key = models.CharField(max_length=4)
    game_name = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    last_run_date = models.DateTimeField('date last run')


class CharacterSheet(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    # Stats version in case we change how they are saved in the future and need to easily check if using the old format.
    stats_version = models.IntegerField(default=0)
    # Currently planning on converting character stats, inventory, etc to a string and putting it here.
    stats = models.CharField(default="", max_length=999999)
