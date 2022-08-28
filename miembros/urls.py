from django.urls import path
from miembros.views import listar_familiares

urlpatterns = [
    path('', listar_familiares),
]
