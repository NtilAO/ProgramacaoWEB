# praias/views.py

from django.shortcuts import render
from .models import Praia, Regiao, Servico

def layout_view(request):
    praias = Praia.objects.all().order_by('nome')
    regioes = Regiao.objects.all().order_by('nome')
    context = {
        'praias': praias,
        'regioes': regioes,
    }
    return render(request, 'praias/layout.html', context)

def praia_view(request, praia_nome):
    praia = Praia.objects.get(nome=praia_nome)
    servicos = praia.servico_set.all()
    regiao = praia.regiao_set.all()
    context = {
        'praia': praia,
        'servicos': servicos,
        'regiao': regiao,
    }
    return render(request, 'praias/praia.html', context)