from django.urls import path
from PeliMundo.views import *

urlpatterns = [
    path('', home),
    path('gestionPeliculas/', gestionPeliculas)
]