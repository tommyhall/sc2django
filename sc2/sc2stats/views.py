from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from sc2.forms import BalanceReportSearchForm
from sc2stats.models import Player, Map, Match


def index(request):
    """ The home/index page """

    # from the django docs, try:
    # question = get_object_or_404(Question, pk=question_id)

    # player_list = Player.objects.order_by('player_id')[:3]
    # context_dict = {'heart': "<3", 'player_list': player_list}
    context_dict = {}
    return render(request, 'sc2stats/index.html', context_dict)


def about(request):
    """ The about page """
    context_dict = {}
    return render(request, 'sc2stats/about.html', context_dict)


def playerstats(request):
    """ The page for displaying player statistics """

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


def balancereport(request):
    """ The page for generating balance reports """

    form = BalanceReportSearchForm()
    message = "no no"

    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = BalanceReportSearchForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required

            map_id = form.cleaned_data.get('map_name')
            if map_id:
                matches = Match.objects.filter(Q(map_id=map_id))

            season = form.cleaned_data.get('season')
            if season:
                matches = matches.filter(Q(season=season))

            league = form.cleaned_data.get('league')
            if league:
                matches = matches.filter(Q(league=league))

            if len(matches) > 0:
                message = "ya hi got something! {0} matches out of {1}".format(len(matches), len(Match.objects.all()))
            else:
                message = "i hear what you're saying but nothing there, def a better way to say this"

    context_dict = {'form': form, 'message': message}

    return render(request, 'sc2stats/balancereport.html', context_dict)
