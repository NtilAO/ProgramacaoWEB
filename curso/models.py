# curso/models.py
from django.db import models

# Create your models here.
class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    ects = models.PositiveIntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=20)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docente)
    linguagens = models.ManyToManyField(LinguagemProgramacao)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_utilizadas = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    video_link = models.URLField()
    github_link = models.CharField(max_length=200)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    linguagens = models.ManyToManyField(LinguagemProgramacao)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=200)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome