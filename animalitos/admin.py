from django.contrib import admin

# Register your models here.

from .models import Colaborador,Animal,Protectora

misModelos = [
    Colaborador,
    Animal,
    Protectora]
admin.site.register(misModelos)
