from django.contrib import admin

from teams.models import Team
from teams.models import PlayerShip


class PlayerAdmin(admin.StackedInline):
    model = PlayerShip
    

class TeamAdmin(admin.ModelAdmin):
    model = Team
    inlines = [PlayerAdmin]
    list_display = ['id', 'name']

    
admin.site.register(Team, TeamAdmin)