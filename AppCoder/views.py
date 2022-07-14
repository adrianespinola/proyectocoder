from django.shortcuts import render
from AppCoder.models import curso
from django.http import HttpResponse

# Create your views here.



def curso(self):
    curso=curso(nombre="django",comision=1536)
    curso.save()
    texto= f("Curso creado: {curso.nombre} {curso.comision}")
    return HttpResponse(texto)