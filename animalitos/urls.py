from django.urls import path
from . import views

urlpatterns = [
    path('animales/', views.list_animales, name='list_animales'),
    path('', views.list_Protectoras, name="list_Protectoras"),
    path('', views.list_Colaboradores, name="list_Colaboradores")
]