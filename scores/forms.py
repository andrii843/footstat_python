from django import forms
from django.forms import formset_factory
from django.forms import inlineformset_factory

from scores.models import Score
from users.models import User
from teams.models import PlayerShip


class ScoreForm(forms.ModelForm):
    to_user = forms.CharField(widget=forms.HiddenInput())
    value = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Оцінка',}
    ))

    class Meta:
        model = Score
        fields = ('value', 'to_user')
        
        
ScoreFormset = inlineformset_factory(PlayerShip, Score, fields=('value', 'to_user'), extra=3, fk_name='from_user')
#ScoreFormset = formset_factory(Score, ScoreForm)

#https://github.com/andrii843/footstat_python.git