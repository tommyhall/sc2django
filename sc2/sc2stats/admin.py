from django.contrib import admin
from sc2stats.models import Player, Map, Match

# Register models

admin.site.register(Player)
admin.site.register(Map)
admin.site.register(Match)
