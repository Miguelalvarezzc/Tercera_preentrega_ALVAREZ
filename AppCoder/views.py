from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def inicio(request):
    return render(request,"AppCoder/inicio.html")

def profesores(request):
    if request.method=="POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profesor=Profesor(nombre=nombre,apellido=apellido,email=email,profesion=profesion)
            profesor.save()
            mensaje="Profesor creado"           
        else:
            mensaje="Datos invalidos"
        formulario_profesor=ProfesorForm()
        return render(request,"AppCoder/profesores.html", {"mensaje":mensaje,"formulario": formulario_profesor})
    else:
        formulario_profesor=ProfesorForm()
    return render(request,"AppCoder/profesores.html", {"formulario": formulario_profesor, "profesores": profesores})


def cursos(request):
    if request.method=="POST":
        form=CursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            comision=info["comision"]
            curso=Curso(nombre=nombre,comision=comision)
            curso.save()
            mensaje="Curso creado"           
        else:
            mensaje="Datos invalidos"
        formulario_curso=CursoForm()
        return render(request, "AppCoder/cursos.html", {"mensaje":mensaje, "formulario": formulario_curso})
    else:
        formulario_curso=CursoForm()
    return render(request, "AppCoder/cursos.html", {"formulario": formulario_curso, "cursos": cursos})


def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html" )

def buscar (request):
    comision=request.GET["comision"]
    if comision!="":
        return render(request,"AppCoder/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"mensaje": "No ingresaste información"})

def estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            estudiante=Estudiante(nombre=nombre,apellido=apellido,email=email)
            estudiante.save()
            mensaje="Estudiante registrado"           
        else:
            mensaje="Datos invalidos"
        formulario_estudiante=EstudianteForm()
        return render(request, "AppCoder/estudiantes.html", {"mensaje":mensaje, "formulario": formulario_estudiante})
    else:
        formulario_estudiante=EstudianteForm()
    return render(request, "AppCoder/estudiantes.html", {"formulario": formulario_estudiante, "estudiantes":estudiantes})