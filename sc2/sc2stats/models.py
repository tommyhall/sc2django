from django.db import models


class Player(models.Model):
    """ A model representing a StarCraft 2 player """

    player_id = models.CharField(max_length=128, unique=True)
    race = models.CharField(max_length=10)

    def __unicode__(self):
        return self.player_id


class Map(models.Model):
    """ A model representing a StarCraft 2 map """

    map_id = models.CharField(max_length=128, unique=True)
    map_size = models.IntegerField(default=2)

    def __unicode__(self):
        return self.map_id


class Match(models.Model):
    """ A model representing a StarCraft 2 match """

    match_id = models.IntegerField(unique=True)
    map_id = models.CharField(max_length=128)
    player_1 = models.CharField(max_length=128)
    player_2 = models.CharField(max_length=128)
    winner = models.CharField(max_length=128)
    season = models.CharField(max_length=128)  # e.g. '2015S3'
    league = models.CharField(max_length=128)  # e.g. 'GSL'
    expansion = models.CharField(max_length=128)  # e.g. 'Heart of the Swarm'

    def __unicode__(self):
        return unicode(self.match_id)
