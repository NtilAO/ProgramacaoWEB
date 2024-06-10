# bandas/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'bandas'
urlpatterns = [
  path('', views.layout_view, name='layout_url'),
  path('banda/<str:banda_nome>/',views.banda_view,name='banda_url'),
  path('album/<str:album_nome>/',views.album_view,name='album_url'),
  path('musica/<str:musica_nome>/',views.musica_view,name='musica_url'),
  path('css/',views.css_view,name='css_url')
]
