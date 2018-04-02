from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games:game_details', args=[self.id])