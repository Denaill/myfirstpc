from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre =  models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    cedula = models.CharField(max_length=10)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()
    direccion = models.TextField()
    tipo = models.CharField(max_length=10)
    correo = models.EmailField()
    password = models.CharField(max_length=50)