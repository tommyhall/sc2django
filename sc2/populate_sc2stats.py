import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sc2.settings')

import django
django.setup()

import random
from sc2stats.models import Player, Map, Match


def populate():
    """ Populate the dB for testing """

    # create some players
    players = []
    players.append(add_player(id='PartinG', race='Protoss'))
    players.append(add_player(id='SoS', race='Protoss'))
    players.append(add_player(id='HerO', race='Protoss'))
    players.append(add_player(id='Zest', race='Protoss'))
    players.append(add_player(id='Life', race='Zerg'))
    players.append(add_player(id='Rogue', race='Zerg'))
    players.append(add_player(id='ByuL', race='Zerg'))
    players.append(add_player(id='Solar', race='Zerg'))
    players.append(add_player(id='INnoVation', race='Terran'))
    players.append(add_player(id='Maru', race='Terran'))
    players.append(add_player(id='Mvp', race='Terran'))
    players.append(add_player(id='Dream', race='Terran'))

    # create some maps
    maps = []
    maps.append(add_map(id='Coda LE', size=2))
    maps.append(add_map(id='Terraform LE', size=2))
    maps.append(add_map(id='Moonlight Madness LE', size=2))
    maps.append(add_map(id='Cactus Valley LE', size=4))
    maps.append(add_map(id='Iron Fortress LE', size=4))
    maps.append(add_map(id='Dash and Terminal LE', size=2))

    seasons = ['2015_S1', '2015_S2', '2015_S3', '2014_S1', '2014_S2', '2014_S3']
    leagues = ['GSL', 'SSL']

    # create some matches
    key_id = 0
    for season in seasons:
        for league in leagues:
            for i in xrange(40):
                # randomly grab a map, players, winner, gogo
                map_id = random.choice(maps).map_id
                player_ids = random.sample(players, 2)
                player_1 = player_ids[0].player_id
                player_2 = player_ids[1].player_id
                winner = random.choice(player_ids).player_id
                # gogo
                add_match(id=key_id,
                    map_id=map_id,
                    player_1=player_1,
                    player_2=player_2,
                    winner=winner,
                    season=season,
                    league=league,
                    exp='HotS'
                )
                key_id += 1

    print "done"




    # add_match(id=1,
    #     map_id='Coda LE',
    #     player_1='PartinG',
    #     player_2='Life',
    #     winner='Life',
    #     season='2015S2',
    #     league='GSL',
    #     exp='HotS')
    #
    # add_match(id=2,
    #     map_id='Coda LE',
    #     player_1='SoS',
    #     player_2='Rogue',
    #     winner='SoS',
    #     season='2015S2',
    #     league='SSL',
    #     exp='HotS')
    #
    # add_match(id=3,
    #     map_id='Terraform LE',
    #     player_1='ByuL',
    #     player_2='HerO',
    #     winner='HerO',
    #     season='2015S3',
    #     league='GSL',
    #     exp='HotS')
    #
    # add_match(id=4,
    #     map_id='Terraform LE',
    #     player_1='INnoVation',
    #     player_2='Life',
    #     winner='Life',
    #     season='2015S2',
    #     league='SSL',
    #     exp='HotS')
    #
    # add_match(id=5,
    #     map_id='Moonlight Madness LE',
    #     player_1='Maru',
    #     player_2='SoS',
    #     winner='SoS',
    #     season='2015S2',
    #     league='SSL',
    #     exp='HotS')
    #
    # add_match(id=6,
    #     map_id='Moonlight Madness LE',
    #     player_1='ByuL',
    #     player_2='Mvp',
    #     winner='ByuL',
    #     season='2015S3',
    #     league='GSL',
    #     exp='HotS')
    #
    # add_match(id=7,
    #     map_id='Cactus Valley LE',
    #     player_1='Maru',
    #     player_2='PartinG',
    #     winner='Maru',
    #     season='2015S3',
    #     league='SSL',
    #     exp='HotS')
    #
    # add_match(id=8,
    #     map_id='Cactus Valley LE',
    #     player_1='Mvp',
    #     player_2='Rogue',
    #     winner='Mvp',
    #     season='2015S2',
    #     league='GSL',
    #     exp='HotS')
    #
    # add_match(id=9,
    #     map_id='Iron Fortress LE',
    #     player_1='INnoVation',
    #     player_2='HerO',
    #     winner='INnoVation',
    #     season='2015S3',
    #     league='SSL',
    #     exp='HotS')
    #
    # add_match(id=10,
    #     map_id='Iron Fortress LE',
    #     player_1='SoS',
    #     player_2='HerO',
    #     winner='HerO',
    #     season='2015S3',
    #     league='GSL',
    #     exp='HotS')

def add_player(id, race):
    p = Player.objects.get_or_create(player_id=id)[0]
    p.race=race
    p.save()
    return p

def add_map(id, size):
    m = Map.objects.get_or_create(map_id=id)[0]
    m.map_size=size
    m.save()
    return m

def add_match(id, map_id, player_1, player_2, winner, season, league, exp):
    m = Match.objects.get_or_create(match_id=id)[0]
    m.map_id=map_id
    m.player_1=player_1
    m.player_2=player_2
    m.winner=winner
    m.season=season
    m.league=league
    m.expansion=exp
    m.save()
    return m

if __name__ == '__main__':
    print "Starting sc2stats population script..."
    print "\t(loading dummy data into db)"
    populate()
