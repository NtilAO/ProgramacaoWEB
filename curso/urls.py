# curso/urls.py

from django.urls import path
from . import views

app_name = 'curso'
urlpatterns = [
  path('',views.area_view,name='area_url'),
  path('cursos/',views.cursos_view,name='cursos_url'),
  path('curso/<str:curso_nome>/',views.curso_view,name='curso_url'),
  path('disciplina/<str:disciplina_nome>/',views.disciplina_view,name='disciplina_url'),
  path('projeto/<str:projeto_nome>/',views.projeto_view,name='projeto_url'),
]