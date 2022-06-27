from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    
    #URLS de la App
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('cursos/', cursos, name="cursos"),
    #path('base/', base),
    path('crear-curso/', crear_curso, name="crear-curso"),
    #path('buscar_comision/', buscar_comision, name="buscar_comision"),
    path('crear-profesor/', crear_profesor, name="crear-profesor"),
    path('crear-estudiante/',crear_estudiante, name="crear-estudiante"),
 ]