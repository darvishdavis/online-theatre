from django import forms
from .models import Movies


class FilmForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['title', 'description', 'year', 'image']
