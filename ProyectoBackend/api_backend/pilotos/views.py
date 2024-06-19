from django.http import JsonResponse
from django.shortcuts import render
from pilotos.models import Piloto, Director, Pista
from pilotos.serializers import PilotoSerializer, DirectorSerializer, PistaSerializer
from django.views.generic import CreateView
from pilotos.forms import PilotoForm, DirectorForm, UserForm, PistaForm
# Create your views here.

def get_all_pilotos():
    pilotos = Piloto.objects.all().order_by('name')
    pilotos_serializers = PilotoSerializer(pilotos, many=True)
    return pilotos_serializers.data

def get_all_directors():
    directors = Director.objects.all().order_by('name')
    directors_serializers = DirectorSerializer(directors, many=True)
    return directors_serializers.data

def get_all_pistas():
    pistas = Pista.objects.all().order_by('name')
    pistas_serializers = PistaSerializer(pistas, many=True)
    return pistas_serializers.data

def pilotos_rest(request):
    pilotos = get_all_pilotos()
    return JsonResponse(pilotos, safe=False)

def directors_rest(request):
    directors = get_all_directors()
    return JsonResponse(directors, safe=False)

def pistas_rest(request):
    pistas = get_all_pistas()
    return JsonResponse(pistas, safe=False)

def index_pil(request):
    pilotos = get_all_pilotos()
    directors = get_all_directors()
    pistas = get_all_pistas()
    return render(request, 'index_pil.html', {'pilotos': pilotos, 'directors': directors, 'pistas': pistas})

def users_rest(request):
    return JsonResponse("Ok", safe=False)

class NewPilotoView(CreateView):
    form_class = PilotoForm
    template_name = 'form_pil.html'
    success_url = '/'

class NewDirectorView(CreateView):
    form_class = DirectorForm
    template_name = 'form_dir.html'
    success_url = '/'

class NewPistaView(CreateView):
    form_class = PistaForm
    template_name = 'form_pis.html'
    success_url = '/'

class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_usu.html'
    success_url = '/'
