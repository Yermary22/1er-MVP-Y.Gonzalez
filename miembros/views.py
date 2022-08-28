from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template,Context, loader
from miembros.models import Familiares

def listar_familiares(request):
    queryset = Familiares.objects.all()
    diccionario={'miembros': queryset}
    plantilla = loader.get_template('familiares_list.html')
    documento_html = plantilla.render(diccionario)
       
    return HttpResponse(documento_html)