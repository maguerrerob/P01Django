from django.shortcuts import render
from .models import Animal
# Create your views here.

def list_animales(request):
    animales = Animal.objects.all()
    return render(request, 'animalitos/animales.html', {'animales_mostrar':animales})