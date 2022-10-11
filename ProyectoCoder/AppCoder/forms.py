
from django import forms


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
    fechaDeEntrega = forms.DateField(label="Ingrese fecha de entrega")
    entregado = forms.BooleanField(label="Check")
    