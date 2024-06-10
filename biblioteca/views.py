from django.shortcuts import render

# Create your views here.
from .models import *


def index_view(request):
    context = {
        'autores': Autor.objects.all().order_by('nome'),
    }
    return render(request, "biblioteca/index.html", context)



def autor_view(request, autor_id):
    context = {
        'autor': Autor.objects.get(id=autor_id),
    }
    return render(request, "biblioteca/autor.html", context)



def livro_view(request, livro_id):
    context = {
        'livro': Livro.objects.get(id=livro_id),
    }
    return render(request, "biblioteca/livro.html", context)


def generos_view(request):
    context = {
        'generos': Livro.objects.values_list('genero', flat=True).distinct()
        }
    return render(request, "biblioteca/generos.html", context)


def genero_view(request, genero):
    context = {
        'genero': genero,
        'livros': Livro.objects.filter(genero=genero),
    }
    return render(request, "biblioteca/genero.html", context)