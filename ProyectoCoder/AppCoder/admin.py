from django.contrib import admin

from AppCoder.models import Curso, Entregable, Estudiante, Profesor, Avatar

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Avatar)
