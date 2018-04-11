from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from scores.models import Score
from scores.forms import ScoreFormset

from games.models import Game
from teams.models import PlayerShip

# Create your views here.

def score_add_view(request):
    if request.method == 'POST':
        formset = ScoreFormset(request.POST)
        if formset.is_valid():
            formset.save(commit=False)
#            for f in formset:
#                f.from_user = request.user
                
            print(formset)
            
            return redirect('games:home')
    else:
        
        game = Game.objects.get(id=1)
        users_one = PlayerShip.objects.filter(Q(team = game.team_one) | Q(team = game.team_two)).exclude(user = request.user)
#        users_two = PlayerShip.objects.filter().exclude(user = request.user)
        print(users_one)
        
        init = []
        for user in users_one:
            line = {
                'to_user': user
            }
            init.append(line)
            
        print(init)
        print(ScoreFormset)
        formset = ScoreFormset(initial=init)
        print(formset)
        i = 0
        for form in formset:
#            form.fields['value'].initial = 23

#            form.fields['to_user'].initial = init[i]['to_user'].id
            form.fields['to_user'].queryset = users_one
            i += 1
        
    return render(request, 'scores/create.html', {'formset': formset})

