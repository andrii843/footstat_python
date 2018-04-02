from django.shortcuts import render

from games.models import Game


def home_view(request):
    games = Game.objects.all()
#    print(games[0].team_one.users.all())
    context = {
        'games': games,
    }

    return render(request, 'games/home.html', context)

def game_details_view(request, game_id):
    game = Game.objects.get(id=game_id)
    
#    print(game[0].team_one.users.all())
    context = {
        'game': game
    }

    return render(request, 'games/game_details.html', context)
#dscsc    prefetch_related('team_one__users').