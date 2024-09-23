from django.db import models
from django.core.validators import validate_email

class Negocio(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField() 
    horario = models.CharField(max_length=255)  # Consider a better solution for schedules
    telefono = models.CharField(max_length=20)  # Add phone number validation
    email = models.EmailField(validators=[validate_email])

    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='negocios/images/')  # Specify upload directory
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)