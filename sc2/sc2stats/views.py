from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from sc2stats.models import Player, Map, Match


def index(request):
    """ The home/index page """

    # from the django docs:
    # question = get_object_or_404(Question, pk=question_id)

    player_list = Player.objects.order_by('player_id')[:3]

    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {'heart': "<3", 'player_list': player_list}

    # Return a rendered response to send to the client.
    return render(request, 'sc2stats/index.html', context_dict)


def about(request):
    # return HttpResponse("""
    # this is the about page for sc2stats <br/>
    # back to <a href='/sc2stats'>home</a>
    # """)
    context_dict = {}
    return render(request, 'sc2stats/about.html', context_dict)


def playerstats(request):

    all_players = []
    player_list = Player.objects.all()

    for player in player_list:
        matches_played = Match.objects.filter(
            Q(player_1=player.player_id) |
            Q(player_2=player.player_id))
        matches_won = Match.objects.filter(winner=player.player_id)
        win_pct = float(len(matches_won)) / float(len(matches_played))
        win_pct = round(win_pct * 100, 2)
        player_tuple = (player.player_id, player.race, win_pct)
        all_players.append(player_tuple)

    top_players = sorted(all_players, key=lambda x: x[2], reverse=True)[:3]

    context_dict = {'top_players': top_players, 'all_players': all_players}
    return render(request, 'sc2stats/playerstats.html', context_dict)


# def win_rate_report(request):
#     """ A page that reports the win rate for each player """
#
#     all_players = []
#     player_list = Player.objects.all()
#
#     for player in player_list:
#         matches_played = Match.objects.filter(
#             Q(player_1=player.player_id) |
#             Q(player_2=player.player_id))
#         matches_won = Match.objects.filter(winner=player.player_id)
#         win_pct = float(len(matches_won)) / float(len(matches_played))
#         win_pct = round(win_pct * 100, 2)
#         player_tuple = (player.player_id, player.race, win_pct)
#         all_players.append(player_tuple)
#
#     top_players = sorted(all_players, key=lambda x: x[2], reverse=True)[:3]
#
#     context_dict = {'top_players': top_players, 'all_players': all_players}
#
#     return render(request, 'sc2stats/win_rate_report.html', context_dict)
