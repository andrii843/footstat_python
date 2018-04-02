from django.db import models

from teams.models import Team


class Game(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    note = models.TextField()
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='first_team')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='second_team')

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
