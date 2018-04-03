from django.shortcuts import render

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
    if request.method == 'GET':
        form = GameForm()
        context = {
            'form': form
        }
        return render(request, 'games/create.html', context)