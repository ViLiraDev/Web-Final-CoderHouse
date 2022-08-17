from django.contrib import admin
from .models import Film, FilmGenre
# Register your models here.

admin.site.register(Film)
admin.site.register(FilmGenre)