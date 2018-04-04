from django.shortcuts import render

from scores.models import Score
from scores.forms import ScoreFormset

from games.models import Game
from teams.models import PlayerShip

# Create your views here.

def score_add_view(request):
    if request.method == 'POST':
        form = ScoreFormset(request.POST)
            
    else:
        
        game = Game.objects.get(id=3)
        users_one = PlayerShip.objects.filter(team = game.team_one).exclude(user = request.user)
        users_two = PlayerShip.objects.filter(team = game.team_two).exclude(user = request.user)
        print(users_one)
        print(users_two)
        
        init = []
        for user in users_one:
            line = {
                'to_user': user.id
            }
            init.append(line)
        for user in users_two:
            line = {
                'to_user': user.id
            }
            init.append(line)
            
        print(init)
        print(ScoreFormset)
        formset = ScoreFormset(initial=init)
        
    return render(request, 'scores/create.html', {'formset': formset})

