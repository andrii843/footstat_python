from django import forms

from games.models import Game


class GameForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Назва гри', 'id': 'name'}
    ))
    date = forms.DateField()
    note = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Напиши щось, щоб потім міг одразу згадати про цю гру', 'id': 'note'}
    ))

    class Meta:
        model = Game
        fields = ('name', 'date', 'note', 'team_one', 'team_two')