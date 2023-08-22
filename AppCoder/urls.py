from django.urls import path
from .views import *

urlpatterns = [
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('cursos/', cursos, name="cursos"),
    path('busquedacomision/', busquedaComision, name="busquedaComision"),
    path('buscar/', buscar, name="buscar"),
]