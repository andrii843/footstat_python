from django.urls import path

from scores.views import score_add_view

app_name = 'scores'

urlpatterns = [    
    path('add/', score_add_view, name='score_add'),
]