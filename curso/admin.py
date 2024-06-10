# curso/admin.py

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AreaCientifica)
admin.site.register(Docente)
admin.site.register(Disciplina)
admin.site.register(Projeto)
admin.site.register(LinguagemProgramacao)
admin.site.register(Curso)