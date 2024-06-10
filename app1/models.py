from django.db import models

# Create your models here.
class Pessoa(models.Model):
    primeiroNome = models.CharField(max_length=200)
    segundoNome = models.CharField(max_length=200)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.primeiroNome} {self.segundoNome} - {self.idade} anos'