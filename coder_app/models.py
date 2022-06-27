from tabnanny import verbose
from django.db import models

# Create your models here.

class Curso(models.Model):

    # id por defecto
    nombre = models.CharField("Nombre" ,max_length=30) # Texto
    comision = models.IntegerField("Comisión")

class Estudiante(models.Model):

    # id por defecto
    nombre = models.CharField("Nombre" ,max_length=30) # Texto
    apellido = models.CharField("Apellido" ,max_length=30) # Texto
    email = models.EmailField("email" ,blank=True, null=True) # Email - Opcional

class Profesor(models.Model):

    # id por defecto
    nombre = models.CharField("Nombre" ,max_length=30) # Texto
    apellido = models.CharField("Apellido" ,max_length=30) # Texto
    email = models.EmailField("email" ,blank=True, null=True) # Email - Opcional
    profesion = models.CharField("Profesion" ,max_length=30)
    
    class Meta:
        verbose_name_plural = "Profesores"

