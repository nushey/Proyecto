from http.client import NON_AUTHORITATIVE_INFORMATION, HTTPResponse
from typing import List
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import request
from django.template import loader
from django.views.generic import ListView

from AppCoder.models import Estudiante, Curso, Profesor, Entregable, Avatar
from AppCoder.forms import (
    formulario_Cursos,
    formulario_Entregables,
    formulario_Estudiantes,
    formulario_Profesores,
    Registro,
    UserEditForm,
    AvatarForm
)
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
    ListView,
)
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Inicio
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        contexto = {"url":avatares[0].imagen.url}
    else:
        contexto = {}
    return render(request, "AppCoder/inicio.html", contexto)


# Estudiantes

@login_required
def estudiante(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        contexto = {"url":avatares[0].imagen.url}
    else:
        contexto = {}
    return render(request, "AppCoder/estudiante.html", contexto)

class EstudianteList(LoginRequiredMixin, ListView):

    login_url = "/AppCoder/login"
    redirect_field_name = "Login"
    model = Estudiante
    template_name = "AppCoder/estudiante_lista.html"

    def get_context_data(self, **kwargs):
        avatar = Avatar.objects.filter(user=self.request.user).first()
        contexto = super().get_context_data(**kwargs)
        if avatar is not None:
            contexto["avatar"] = avatar.imagen.url
        else:
            contexto["avatar"] = None
        return contexto


class EstudianteDetalle(DetailView):

    model = Estudiante
    template_name = "AppCoder/estudiante_detalle.html"

    def get_context_data(self, **kwargs):
        avatar = Avatar.objects.filter(user=self.request.user).first()
        contexto = super().get_context_data(**kwargs)
        if avatar is not None:
            contexto["avatar"] = avatar.imagen.url
        else:
            contexto["avatar"] = None
        return contexto


class EstudianteCreacion(CreateView):

    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = "/AppCoder/estudiante"

    def get_context_data(self, **kwargs):
        avatar = Avatar.objects.filter(user=self.request.user).first()
        contexto = super().get_context_data(**kwargs)
        if avatar is not None:
            contexto["avatar"] = avatar.imagen.url
        else:
            contexto["avatar"] = None
        return contexto


class EstudianteUpdate(UpdateView):

    model = Estudiante
    success_url = "/AppCoder/estudiante_lista"
    fields = ["nombre", "apellido", "email"]

    def get_context_data(self, **kwargs):
        avatar = Avatar.objects.filter(user=self.request.user).first()
        contexto = super().get_context_data(**kwargs)
        if avatar is not None:
            contexto["avatar"] = avatar.imagen.url
        else:
            contexto["avatar"] = None
        return contexto


class EstudianteDelete(DeleteView):

    model = Estudiante
    success_url = "/AppCoder/estudiantes"

    def get_context_data(self, **kwargs):
        avatar = Avatar.objects.filter(user=self.request.user).first()
        contexto = super().get_context_data(**kwargs)
        if avatar is not None:
            contexto["avatar"] = avatar.imagen.url
        else:
            contexto["avatar"] = None
        return contexto


# Profesores

@login_required
def profesor(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        contexto = {"url":avatares[0].imagen.url}
    else:
        contexto = {}
    return render(request, "AppCoder/profesores.html", contexto)

class ProfesorList(LoginRequiredMixin, ListView):

    login_url = "/AppCoder/login"
    redirect_field_name = "Login"
    model = Profesor
    template_name = "AppCoder/profesores_lista.html"


class ProfesorDetalle(DetailView):

    model = Profesor
    template_name = "AppCoder/profesor_detalle.html"


class ProfesorCreacion(CreateView):

    model = Profesor
    fields = ["nombre", "apellido", "email", "profesion"]
    success_url = "/AppCoder/profesores"


class ProfesorUpdate(UpdateView):

    model = Profesor
    success_url = "/AppCoder/profesores"
    fields = ["nombre", "apellido", "email", "profesion"]


class ProfesorDelete(DeleteView):

    model = Profesor
    success_url = "/AppCoder/profesores"


# Cursos

@login_required
def curso(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        contexto = {"url":avatares[0].imagen.url}
    else:
        contexto = {}
    return render(request, "AppCoder/cursos.html", contexto)

class CursoList(LoginRequiredMixin, ListView):

    login_url = "/AppCoder/login"
    redirect_field_name = "Login"
    model = Curso
    template_name = "AppCoder/cursos_lista.html"


class CursoDetalle(DetailView):

    model = Curso
    template_name = "AppCoder/curso_detalle.html"


class CursoCreacion(CreateView):

    model = Curso
    fields = ["nombre", "camada"]
    success_url = "/AppCoder/cursos"


class CursoUpdate(UpdateView):

    model = Curso
    success_url = "/AppCoder/cursos"
    fields = ["nombre", "camada"]


class CursoDelete(DeleteView):

    model = Curso
    success_url = "/AppCoder/cursos"


# Entregables

@login_required
def entregable(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        contexto = {"url":avatares[0].imagen.url}
    else:
        contexto = {}
    return render(request, "AppCoder/entregables.html", contexto)

class EntregableList(LoginRequiredMixin, ListView):

    login_url = "/AppCoder/login"
    redirect_field_name = "Login"
    model = Entregable
    template_name = "AppCoder/entregables_lista.html"


class EntregableDetalle(DetailView):

    model = Entregable
    template_name = "AppCoder/entregable_detalle.html"


class EntregableCreacion(CreateView):

    model = Entregable
    fields = ["nombre", "fecha", "entregado"]
    success_url = "/AppCoder/entregables"


class EntregableUpdate(UpdateView):

    model = Entregable
    success_url = "/AppCoder/entregables"
    fields = ["nombre", "fecha", "entregado"]


class EntregableDelete(DeleteView):

    model = Entregable
    success_url = "/AppCoder/entregables"


def busqueda(request):
    return render(request, "AppCoder/busqueda.html")


def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(
            request,
            "AppCoder/resultadosPorBusqueda.html",
            {"cursos": cursos, "camada": camada},
        )
    else:
        respuesta = "No enviaste datos"

    return render(request, "AppCoder/inicio.html", {"respuesta": respuesta, "pag": 6})


def login_request(request):

    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render(
                    request,
                    "AppCoder/inicio.html",
                    {"mensaje": f"Bienvenido {usuario}"},
                )
            else:
                return render(
                    request,
                    "AppCoder/login.html",
                    {"mensaje": "Error, datos incorrectos"},
                )

        else:
            return render(
                request,
                "AppCoder/login.html",
                {"mensaje": "Los datos que ha ingresado son incorrectos"},
            )

    form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(
                request,
                "AppCoder/registro.html",
                {"mensaje": f"Tu usuario ha sido creado, bienvenido"},
            )

    else:
        form = Registro()

    return render(request, "AppCoder/registro.html", {"form": form})


@login_required
def editarPerfil(request):

    user = request.user
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method != "POST":
        form = UserEditForm(initial={"email": user.email})
    else:
        form = UserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.username = data["username"]
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "AppCoder/inicio.html")            
    
    contexto = {"user": user, "form": form,"url":avatares[0].imagen.url}
    return render(request, "AppCoder/editarPerfil.html", contexto)

#Agregar Avatar
@login_required
def agregar_avatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "AppCoder/inicio.html")
    contexto = {"form":form, "url":avatares[0].imagen.url}
    return render(request, "AppCoder/avatar_form.html", contexto)



