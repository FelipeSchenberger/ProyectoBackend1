from django.db import models

# Create your models here.


class Piloto(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    team = models.CharField(max_length=128)
    worldchampion = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.name}'
    
class Director(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    team = models.CharField(max_length=128)
    worldchampion = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.name}'
    
class Pista(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    largo = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.id} - {self.name}'

class User(models.Model):
    name = models.CharField(max_length=128)
    pilotos = models.ManyToManyField(Piloto, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    pistas = models.ManyToManyField(Pista, blank=True)

    def __str__(self):
        return self.name