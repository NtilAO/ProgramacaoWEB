# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('why/', views.why_view),
    path('reason/', views.reason_view),
    path('sleep/', views.sleep_view),
]