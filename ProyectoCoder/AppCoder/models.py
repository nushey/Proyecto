from unittest.util import _MAX_LENGTH
from urllib.parse import MAX_CACHE_SIZE
from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()



class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    pass