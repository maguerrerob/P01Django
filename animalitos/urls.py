from django.urls import path
from . import views

urlpatterns = [
    path("animales/", views.vistaAnimal, name="vistaAnimal"),
    path("colaboradores/", views.vistaColaborador, name="vistaColaborador"),
    path("protectoras/", views.vistaProtectora, name="vistaProtectora"),
]