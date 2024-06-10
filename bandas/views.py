# bandas/views.py

from django.shortcuts import render
from .models import Banda, Album, Musica

def layout_view(request):
    bandas = Banda.objects.all().order_by('nome')
    context = {
        'bandas': bandas,
    }
    return render(request, 'bandas/layout.html', context)

def banda_view(request, banda_nome):
    banda = Banda.objects.get(nome=banda_nome)
    albuns = banda.album_set.all()
    context = {
        'banda': banda,
        'albuns': albuns,
    }
    return render(request, 'bandas/banda.html', context)

def album_view(request, album_nome):
    album = Album.objects.get(tituloAlbum=album_nome)
    musicas = album.musica_set.all()
    context = {
      'album': album,
      'musicas': musicas,
    }
    return render(request, 'bandas/album.html', context)

def musica_view(request, musica_nome):
   context = {
      'musica': Musica.objects.get(tituloMusica=musica_nome),
   }
   return render(request, 'bandas/musica.html', context)

def css_view(request):
    return render(request, 'bandas/html5-css.html')