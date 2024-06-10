from django.contrib import admin
from .models import Banda, Album, Musica

# Register your models here.
admin.site.register(Banda)
admin.site.register(Album)
admin.site.register(Musica)