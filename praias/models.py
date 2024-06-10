from django.db import models

# Create your models here.
class Praia(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Regiao(models.Model):
    nome = models.CharField(max_length=200)
    praias = models.ManyToManyField(Praia)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=200)
    praias = models.ManyToManyField(Praia)

    def __str__(self):
        return self.nome