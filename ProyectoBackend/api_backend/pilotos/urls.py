from django.urls import path
from pilotos import views

urlpatterns = [
    path('', views.index_pil, name='index_pil'),
    path('pilotos_rest/', views.pilotos_rest, name='pilotos_rest'),
    path('directors_rest/', views.directors_rest, name='directors_rest'),
    path('pistas_rest/', views.pistas_rest, name='pistas_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    path('new_piloto/', views.NewPilotoView.as_view(), name='new_piloto'),
    path('new_director/', views.NewDirectorView.as_view(), name='new_director'),
    path('new_pista/', views.NewPistaView.as_view(), name='new_pista'),
    path('new_userp/', views.NewUserView.as_view(), name='new_userp'),
]
