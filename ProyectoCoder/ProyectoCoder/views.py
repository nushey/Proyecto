from contextvars import Context
from pipes import Template
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader

import random

import datetime



def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludar_con_nombre(request, nombre, edad):
    hoy = datetime.datetime.now()
    return HttpResponse(f"Buenas noches: {nombre.title()} <br> Hoy es {hoy} <br> tu edad es: {edad} ")

def numero_random(request):
    return HttpResponse(random.random())

def saludar_desde_template(self):

    nombre = "Nahuel"
    apellido = "Zeballos"

    miDict = {"nom": nombre, "ap": apellido}

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(miDict)
    return HttpResponse(documento)