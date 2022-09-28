from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from AppCoder.models import Estudiante

def mostrar_inicio(request):

    estudiante = Estudiante(nombre="Ezequiel", apellido="Figueroa", email="a@coder.com")
    contexto = {"estudiante_1": estudiante}
    return render(request, "AppCoder/inicio.html", contexto)