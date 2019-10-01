from django.db import models
from apps.usuarios.models import Usuarios
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=10)
    id_producto = models.CharField(max_length=10)
    descripcion = models.TextField()
    imagen = models.ImageField()
    valor = models.IntegerField()
    plataforma = models.CharField(max_length=10)
    fecha_publicacion = models.DateField()
    usuarios = models.ForeignKey(Usuarios, null=True, blank=True, on_delete=models.CASCADE)

