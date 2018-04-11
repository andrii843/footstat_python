from django.db import models

from teams.models import PlayerShip


class Score(models.Model):
    value = models.DecimalField(max_digits=6, decimal_places=4)
    from_user = models.ForeignKey(PlayerShip, on_delete=models.CASCADE, related_name='from_users')
    to_user = models.ForeignKey(PlayerShip, on_delete=models.CASCADE, related_name='to_users')

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
        unique_together = ('from_user', 'to_user')
