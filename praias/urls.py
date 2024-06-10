# praias/urls.py

from django.urls import path
from . import views

app_name = 'praias'
urlpatterns = [
  path('', views.layout_view, name='layout_url'),
  path('praia/<str:praia_nome>/',views.praia_view,name='praia_url'),
]