from django.urls import path

from games.views import home_view

app_name = 'games'

urlpatterns = [
    path('', home_view, name='home')
]