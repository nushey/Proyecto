"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    # Cursos
    path("cursos/", views.curso, name="Cursos"),
    path("curso_lista/", views.CursoList.as_view(), name="ListaCursos"),
    path("r'(?P<pk>\d+)^$'curso", views.CursoDetalle.as_view(), name="DetalleCursos"),
    path("curso-nuevo/", views.CursoCreacion.as_view(), name="CrearCursos"),
    path("editar-curso/<pk>", views.CursoUpdate.as_view(), name="EditarCursos"),
    path("borrar-curso/<pk>", views.CursoDelete.as_view(), name="BorrarCursos"),
    # Profesores
    path("profesores/", views.profesor, name="Profesores"),
    path("profesores_lista/", views.ProfesorList.as_view(), name="ListaProfesores"),
    path(
        "r'(?P<pk>\d+)^$'profesor",
        views.ProfesorDetalle.as_view(),
        name="DetalleProfesores",
    ),
    path("profesor-nuevo/", views.ProfesorCreacion.as_view(), name="CrearProfesores"),
    path(
        "editar-profesor/<pk>", views.ProfesorUpdate.as_view(), name="EditarProfesores"
    ),
    path(
        "borrar-profesor/<pk>", views.ProfesorDelete.as_view(), name="BorrarProfesores"
    ),
    # Estudiantes
    path("estudiante/", views.estudiante, name="Estudiantes"),
    path("estudiante_lista/", views.EstudianteList.as_view(), name="ListaEstudiantes"),
    path(
        "r'(?P<pk>\d+)^$'estudiante",
        views.EstudianteDetalle.as_view(),
        name="DetalleEstudiantes",
    ),
    path(
        "estudiante-nuevo/", views.EstudianteCreacion.as_view(), name="CrearEstudiantes"
    ),
    path(
        "editar-estudiante/<pk>",
        views.EstudianteUpdate.as_view(),
        name="EditarEstudiantes",
    ),
    path(
        "borrar-estudiante/<pk>",
        views.EstudianteDelete.as_view(),
        name="BorrarEstudiantes",
    ),
    # Entregables
    path("entregables/", views.entregable, name="Entregables"),
    path("entregable_lista/", views.EntregableList.as_view(), name="ListaEntregables"),
    path(
        "r'(?P<pk>\d+)^$'entregable",
        views.EntregableDetalle.as_view(),
        name="DetalleEntregables",
    ),
    path(
        "entregable-nuevo/", views.EntregableCreacion.as_view(), name="CrearEntregables"
    ),
    path(
        "editar-entregable/<pk>",
        views.EntregableUpdate.as_view(),
        name="EditarEntregables",
    ),
    path(
        "borrar-entregable/<pk>",
        views.EntregableDelete.as_view(),
        name="BorrarEntregables",
    ),
    # Login
    path("login", views.login_request, name="Login"),
    # Registro
    path("register", views.register, name="Register"),
    path(
        "logout",
        LogoutView.as_view(template_name="AppCoder/logout.html"),
        name="Logout",
    ),
    # EditarPerfil
    path("editarPerfil", views.editarPerfil, name="EditarPerfil"),
    # Agregar Avatar
    path("agregar_avatar", views.agregar_avatar, name="AgregarAvatar")
]
