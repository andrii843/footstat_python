from django.db import models
from users.models import User


class Team(models.Model):

    name = models.CharField(
        max_length=255
    )
    is_win = models.BooleanField(
        default=False
    )
    users = models.ManyToManyField(
        User,
        through='PlayerShip',
        related_name='players'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class PlayerShip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)