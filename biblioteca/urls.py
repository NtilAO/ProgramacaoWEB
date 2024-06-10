from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name="autores"),
    path('autor/<int:autor_id>/', views.autor_view, name="autor"),
    path('livro/<int:livro_id>/', views.livro_view, name="livro"),
    path('generos/', views.generos_view, name="generos"),
    path('genero/<str:genero>', views.genero_view, name="genero"),
]