from rest_framework import serializers

from pilotos.models import Piloto, Director, Pista


class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = ['name', 'number', 'team', 'worldchampion']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'country', 'team', 'worldchampion']

class PistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pista
        fields = ['name', 'country', 'largo']


