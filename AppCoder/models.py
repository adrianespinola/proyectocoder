from django.db import models

# Create your models here.

class curso(models.Model):

    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class estudiante(models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fechadeentrega= models.DateField()
    entregado= models.BooleanField()
