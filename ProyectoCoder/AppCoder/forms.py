from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar


class formulario_Cursos(forms.Form):

    nombre = forms.CharField(label="Ingrese nombre curso")
    camada = forms.IntegerField(label="Ingrese camada")


class formulario_Estudiantes(forms.Form):

    nombre = forms.CharField(label="Ingrese nombre estudiante")
    apellido = forms.CharField(label="Ingrese apellido estudiante")
    email = forms.EmailField(label="Ingrese e-mail estudiante")


class formulario_Profesores(forms.Form):

    nombre = forms.CharField(label="Ingrese su nombre")
    apellido = forms.CharField(label="Ingrese su apellido")
    email = forms.EmailField(label="Ingrese su email")
    profesion = forms.CharField(label="Ingrese su profesion")


class formulario_Entregables(forms.Form):

    nombre = forms.CharField(label="Ingrese nombre")
    fecha = forms.DateField(label="Ingrese fecha de entrega")
    entregado = forms.BooleanField(label="Check")


# Registro


class Registro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita la contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


# Editar Perfil


class UserEditForm(UserCreationForm):

    username = forms.CharField(label="Modificar Usuario")
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña nueva", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]
        help_texts = {k: "" for k in fields}

class AvatarForm(forms.ModelForm):

    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ["imagen", "user"]
