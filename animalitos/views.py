from django.shortcuts import render
from .models import Animal, Colaborador, Protectora

# Create your views here.

def vistaAnimal(request):
    animales = Animal.objects.all()
    return render(request, "animalitos/post_animales.html", {"mostrar_animales": animales})

def vistaColaborador(request):
    colaboradores = Colaborador.objects.all()
    return render(request, "animalitos/post_colaboradores.html", {"mostrar_colaboradores": colaboradores})

def vistaProtectora(request):
    protectoras = Protectora.objects.all()
    return render(request, "animalitos/post_protectoras.html", {"mostrar_protectoras": protectoras})