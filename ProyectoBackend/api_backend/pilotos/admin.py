from django.contrib import admin
from pilotos.models import Piloto, Director, Pista, User

# Register your models here.

admin.site.register(Piloto)
admin.site.register(User)
admin.site.register(Director)
admin.site.register(Pista)
