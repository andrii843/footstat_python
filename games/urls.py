from django.urls import path

from games.views import home_view
from games.views import game_details_view
from games.views import game_add_view

app_name = 'games'

urlpatterns = [
    path('', home_view, name='home'),
    path('<int:game_id>/', game_details_view, name='game_details'),
    path('add/', game_add_view, name='game_add'),
]