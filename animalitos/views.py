from django.shortcuts import render

# Create your views here.

def vistaAnimal(request):
    return render(request, "animalitos/post_animales.html", {})

def vistaColaborador(request):
    return render(request, "animalitos/post_colaboradores.html", {})

def vistaProtectora(request):
    return render(request, "animalitos/post_protectoras.html", {})