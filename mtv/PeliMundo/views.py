from django.shortcuts import render
from .models import Film, FilmGenre

# Create your views here.
def home(request):
    peliculas = Film.objects.all()
    return render(request, 'base.html', {"peliculas": peliculas})

def gestionPeliculas(request):
    peliculas = Film.objects.all()
    return render(request, 'GestionPeliculas.html',{"peliculas": peliculas}) 