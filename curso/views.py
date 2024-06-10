from django.shortcuts import render
from .models import AreaCientifica, Curso, Disciplina, Projeto

# Create your views here.
def area_view(request):
    areas = AreaCientifica.objects.all().order_by('nome')
    context = {
        'areas': areas,
        }
    return render(request, 'curso/layout.html', context)

def cursos_view(request):
    cursos = Curso.objects.all().order_by('nome')
    context = {
        'cursos': cursos,
    }
    return render(request, 'curso/cursos.html', context)

def curso_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplinas = curso.disciplinas.all()
    context = {
        'curso': curso,
        'disciplinas': disciplinas,
        }
    return render(request, 'curso/curso.html', context)

def disciplina_view(request, disciplina_nome):
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projetos = disciplina.projeto_set.all()
    context = {
        'disciplina': disciplina,
        'projetos': projetos,
        }
    return render(request, 'curso/disciplina.html', context)

def projeto_view(request, projeto_nome):
    projeto = Projeto.objects.get(nome=projeto_nome)
    context = {
        'projeto': projeto,
        }
    return render(request, 'curso/projeto.html', context)
