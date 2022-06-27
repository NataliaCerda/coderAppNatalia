from django import forms

class NuevoCurso(forms.Form):
    
    nombre = forms.CharField(max_length=30,label="Curso")
    comision = forms.IntegerField(min_value=0,label="Comisión")

class ProfesorNuevo(forms.Form):

    nombre = forms.CharField(max_length=30,label="Nombre")
    apellido = forms.CharField(max_length=30,label="Apellido")
    email = forms.EmailField(label="Email")
    profesion = forms.CharField(max_length=30,label="Profesion")
    
class EstudianteNuevo(forms.Form):

    # id por defecto
    nombre = forms.CharField(max_length=30,label="Nombre") # Texto
    apellido = forms.CharField(max_length=30,label="Apellido") # Texto
    email = forms.EmailField(label="email") # Email - Opcional
