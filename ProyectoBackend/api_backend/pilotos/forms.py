from django import forms

from pilotos.models import Piloto, Director, Pista, User

class PilotoForm(forms.ModelForm):
       class Meta:
        model = Piloto
        fields = [
            'name',
            'number',
            'team',
            'worldchampion',
        ]

class DirectorForm(forms.ModelForm):
       class Meta:
        model = Director
        fields = [
            'name',
            'country',
            'team',
            'worldchampion',
        ]

class PistaForm(forms.ModelForm):
       class Meta:
        model = Pista
        fields = [
            'name',
            'country',
            'largo'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'pilotos',
            'directors',
            'pistas',
        ]