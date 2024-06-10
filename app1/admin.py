from django.contrib import admin
from django.utils.html import format_html
from .models import Pessoa

# Register your models here.
admin.site.register(Pessoa)