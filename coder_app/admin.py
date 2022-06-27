from django.contrib import admin

# Register your models here.

from .models import *

class CursoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'comision')
    search_fields = ('nombre', 'comision')


class EstudianteAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'email')


class ProfesorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'profesion')
    readonly_fields = ('profesion',)



admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)#, EstudianteAdmin)
admin.site.register(Profesor)#, ProfesorAdmin)
