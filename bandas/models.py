from django.db import models

# Create your models here.
class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome}'

class Album(models.Model):
    tituloAlbum = models.CharField(max_length=100)
    anoDeLancamento = models.IntegerField()
    capa = models.ImageField(null=True, blank=True)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tituloAlbum}'

class Musica(models.Model):
    tituloMusica = models.CharField(max_length=100)
    anoDeLancamento = models.IntegerField()
    link = models.URLField(max_length=200)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    letra = models.TextField(default='', null=True, blank=True)
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.tituloMusica}'