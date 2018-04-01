from django.shortcuts import render

from games.models import Game


def home_view(request):
    games = Game.objects.all()
    print(games[0].team_one.users.all())
    context = {
        'games': games
    }

    return render(request, 'games/home.html', context)