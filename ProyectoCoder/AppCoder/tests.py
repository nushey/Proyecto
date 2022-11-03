from django.test import TestCase
from AppCoder.models import Curso
from AppCoder.models import Profesor

# Create your tests here.

class ViewTestCase(TestCase):
    def test_crear_curso(self):
        Curso.objects.create(nombre="Test 1", camada="01")
        cursos = Curso.objects.all()
        assert len(cursos) == 1
        assert cursos[0].nombre == "Test 1"

    def test_crear_profesores(self):
        Profesor.objects.create(nombre="Julio", apellido="Rodriguez", email="profesor1@coder.com", profesion="Programador")
        Profesor.objects.create(nombre="Mario", apellido="Bros", email="profesor2@coder.com", profesion="Ing. en Sistemas")
        profesores = Profesor.objects.all()
        assert len(profesores) == 2
        assert profesores[0].nombre == "Julio"
        assert profesores[0].apellido == "Rodriguez"
        assert profesores[0].email == "profesor1@coder.com"
        assert profesores[0].profesion == "Programador"

        assert profesores[1].nombre == "Mario"
        assert profesores[1].apellido == "Bros"
        assert profesores[1].email == "profesor2@coder.com"
        assert profesores[1].profesion == "Ing. en Sistemas"

        