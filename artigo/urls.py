# artigo/urls.py

from django.urls import path
from . import views

app_name = 'artigo'
urlpatterns = [
  path('',views.artigos_view,name='artigos_url'),
  path('autores/',views.autores_view,name='autores_url'),
  path('artigo/<str:artigo_nome>/',views.artigo_view,name='artigo_url'),
  path('autor/<str:autor_nome>/',views.autor_view,name='autor_url'),
  path('comentario/<int:comentario_id>/',views.comentario_view,name='comentario_url')
]
