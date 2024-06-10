from django.shortcuts import render
from .models import Artigo, Autor, Comentario

# Create your views here.

def artigos_view(request):
    artigos = Artigo.objects.all().order_by('titulo')
    context = {
        'artigos': artigos,
    }
    return render(request, 'artigo/artigos.html', context)

def autores_view(request):
    autores = Autor.objects.all().order_by('nome')
    context = {
        'autores': autores,
    }
    return render(request, 'artigo/autores.html', context)

def autor_view(request, autor_nome):
    autor = Autor.objects.get(nome=autor_nome)
    artigos = autor.artigo_set.all()
    context = {
      'autor': autor,
      'artigos': artigos,
    }
    return render(request, 'artigo/autor.html', context)

def artigo_view(request, artigo_nome):
    artigo = Artigo.objects.get(titulo=artigo_nome)
    comentarios = artigo.comentario_set.all()
    context = {
        'artigo': artigo,
        'comentarios': comentarios,
    }
    return render(request, 'artigo/artigo.html', context)

def comentario_view(request, comentario_id):
   context = {
      'comentario': Comentario.objects.get(id=comentario_id),
   }
   return render(request, 'artigo/comentario.html', context)