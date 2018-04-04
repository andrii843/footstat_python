from django.shortcuts import render
from django.shortcuts import redirect

from games.models import Game
from games.forms import GameForm


def home_view(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'games/home.html', context)


def game_details_view(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {
        'game': game
    }
    return render(request, 'games/details.html', context)


def game_add_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid:
            game = form.save()
            
            return redirect(game.get_absolute_url())
            
    else:
        form = GameForm()
    
    return render(request, 'games/create.html', {'form': form})