from django.db import models

# Create your models here.
class Negocio(models.Model):
    nombre = models.CharField()
    direccion = models.CharField()
    horario = models.CharField()
    telefono = models.CharField()
    email = models.CharField()

    descripcion = models.TextField()
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
