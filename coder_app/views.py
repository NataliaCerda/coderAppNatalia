from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Curso, Profesor, Estudiante
from .forms import NuevoCurso, ProfesorNuevo, EstudianteNuevo
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"coder_app/index.html")

def crear_curso(request):
    
    if request.method == "POST":

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso = formulario.cleaned_data
            
            curso = Curso(nombre=info_curso["nombre"], comision=info_curso["comision"])

            curso.save()
            
            return redirect("cursos")
        else:
            return render(request,"coder_app/formulario_curso.html",{"form":formulario})
    
    else: #GET y otros
    
        formularioVacio = NuevoCurso()
        
        return render(request,"coder_app/formulario_curso.html",{"form":formularioVacio})
    
def profesores(request):
    
    profesores = Profesor.objects.all()
    
    return render(request,"coder_app/profesores.html",{"profesores":profesores})

def crear_profesor(request):
    
    if request.method == "POST":

        formulario = ProfesorNuevo(request.POST)

        if formulario.is_valid():

            info_profesor = formulario.cleaned_data
            
            profesor = Profesor(nombre=info_profesor["nombre"], apellido=info_profesor["apellido"], email=info_profesor["email"], profesion=info_profesor["profesion"] )

            profesor.save()
            
            return redirect("profesores")
        else:
            return render(request,"coder_app/formulario_profesores.html",{"form":formulario})
    
    else: #GET y otros
    
        formularioVacio = ProfesorNuevo()
        
        return render(request,"coder_app/formulario_profesores.html",{"form":formularioVacio})
    
def estudiantes(request):
    
    estudiantes = Estudiante.objects.all()
    
    return render(request,"coder_app/estudiantes.html",{"estudiantes":estudiantes})

def crear_estudiante(request):
    
    if request.method == "POST":

        formulario = EstudianteNuevo(request.POST)

        if formulario.is_valid():

            info_estudiante = formulario.cleaned_data
            
            estudiante = Estudiante(nombre=info_estudiante["nombre"], apellido=info_estudiante["apellido"], email=info_estudiante["email"] )

            estudiante.save()
            
            return redirect("estudiantes")
        else:
            return render(request,"coder_app/formulario_estudiantes.html",{"form":formulario})
    
    else: #GET y otros
    
        formularioVacio = EstudianteNuevo()
        
        return render(request,"coder_app/formulario_estudiantes.html",{"form":formularioVacio})

def cursos(request):
   
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            cursos = Curso.objects.filter( Q(nombre__icontains=search) | Q(comision__icontains=search) ).values()

            return render(request,"coder_app/cursos.html",{"cursos":cursos, "search":True, "busqueda":search})
    
    cursos = Curso.objects.all()

    return render(request,"coder_app/cursos.html",{"cursos":cursos, "search":False})

def base(request):
    return render(request, "coder_app/base.html",{})

"""
def buscar_comision(request):
    
    if request.method == "POST":
        
        comision = request.POST("comision")
        comisiones = Curso.objects.filter( Q(nombre__icontains=comision) | Q(comision__icontains=comision) ).values()
        
        
        return render(request,"coder_app/buscar_comision.html",{"comisiones":comisiones})
    
    else:
        
        comisiones = [] #Curso.objects.all()

        return render(request,"coder_app/buscar_comision.html",{"cursos":comisiones})
"""
