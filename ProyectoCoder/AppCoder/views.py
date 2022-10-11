from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import request
from django.template import loader

from AppCoder.models import Estudiante, Curso, Profesor, Entregable
from AppCoder.forms import formulario_Entregables, formulario_Cursos, formulario_Profesores, formulario_Estudiantes



def inicio(request):     
    return render(request, "AppCoder/inicio.html", {"pag": 1})




def estudiantes(request):
    if request.method == "POST":
        mi_formulario = formulario_Estudiantes(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiante.save()
            
            return render(request, "AppCoder/inicio.html", {"pag": 2})
    else:
        mi_formulario = formulario_Estudiantes()
    return render(request, "AppCoder/estudiantes.html", {"mi_formulario":mi_formulario, "pag":2})




def profesores(request):
    if request.method == "POST":
        mi_formulario = formulario_Profesores(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            profesor.save()
            
            return render(request, "AppCoder/inicio.html", {"pag": 3})
    else:
        mi_formulario = formulario_Profesores()
    return render(request, "AppCoder/profesores.html", {"mi_formulario":mi_formulario, "pag":3})

def cursos(request):
    if request.method == "POST":
        mi_formulario = formulario_Cursos(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso.save()
            
            return render(request, "AppCoder/inicio.html", {"pag": 4})
    else:
        mi_formulario = formulario_Cursos()
    return render(request, "AppCoder/cursos.html", {"mi_formulario":mi_formulario, "pag":4})

def entregables(request):
    if request.method == "POST":
        mi_formulario = formulario_Entregables(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            entregable = Entregable(nombre=informacion["nombre"], fechaDeEntrega=informacion["fechaDeEntrega"], entregado=informacion["entregado"])
            entregable.save()
            
            return render(request, "AppCoder/inicio.html", {"pag": 5})
    else:
        mi_formulario = formulario_Entregables()
    return render(request, "AppCoder/entregables.html", {"mi_formulario":mi_formulario, "pag":5})

def busqueda(request):
    return render(request, "AppCoder/busqueda.html", {"pag":6})

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos= Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos":cursos, "camada":camada, "pag":6})
    else:
        respuesta="No enviaste datos"
    
    return render(request, "AppCoder/inicio.html", {"respuesta":respuesta, "pag":6})


