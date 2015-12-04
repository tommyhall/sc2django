from django import forms
from sc2stats.models import Player, Map, Match

class BalanceReportSearchForm(forms.Form):
    map_name = forms.ModelChoiceField(queryset=Map.objects.all().order_by('map_id'),
        widget=forms.Select(attrs={'class': 'btn btn-default dropdown-toggle'}),
        empty_label="All",
        required=False)
        #initial=0)  # this sets it to the first choice (no empty choice)

    EMPTY = [('', 'All')]
    SEASON_CHOICES = [
        ('2015_S1', '2015_S1'),
        ('2015_S2', '2015_S2'),
        ('2015_S3', '2015_S3'),
        ('2014_S1', '2014_S1'),
        ('2014_S2', '2014_S2'),
        ('2014_S3', '2014_S3'),
    ]
    SEASON_CHOICES_AND_EMPTY = EMPTY + SEASON_CHOICES
    season = forms.ChoiceField(choices=SEASON_CHOICES_AND_EMPTY,
        widget=forms.Select(attrs={'class': 'btn btn-default dropdown-toggle'}),
        required=False)

    LEAGUE_CHOICES = [
        ('GSL', 'GSL'),
        ('SSL', 'SSL'),
    ]
    LEAGUE_CHOICES_AND_EMPTY = EMPTY + LEAGUE_CHOICES
    league = forms.ChoiceField(choices=LEAGUE_CHOICES_AND_EMPTY,
        widget=forms.Select(attrs={'class': 'btn btn-default dropdown-toggle'}),
        required=False)
