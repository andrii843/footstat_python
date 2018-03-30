from django.db import models
from users.models import User


class Team(models.Model):
    
    users = models.ManyToManyField(
        User,
        through='PlayerShip'
    )
    
#    class Meta:
#        verbose_name = 'Team'
#        verbose_name_plural = 'Teams'
        
class PlayerShip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)