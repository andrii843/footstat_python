from django import forms
from django.forms import formset_factory
from django.forms import inlineformset_factory

from scores.models import Score
from users.models import User
from teams.models import PlayerShip


class ScoreForm(forms.ModelForm):
    to_user = forms.CharField(widget=forms.HiddenInput())
    value = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Оцінка', 'id': 'name'}
    ))

    class Meta:
        model = Score
        fields = ('value', 'to_user')
        
        
ScoreFormset = inlineformset_factory(PlayerShip, Score,  fields=('value', 'to_user'), extra=0)