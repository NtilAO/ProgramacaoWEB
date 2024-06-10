from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    conteudo = models.TextField()
    ano_De_Publicacao = models.PositiveIntegerField(default=0)
    ratings_Total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'"{self.titulo}" | Feito por: {self.autor} | Escrito em: {self.ano_De_Publicacao}'

class Comentario(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    texto = models.TextField()
    ano_Do_Comentario = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Comentário por {self.autor.username} em "{self.artigo.titulo}"'