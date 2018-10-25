from django.db import models

# Create your models here.
class Persona(models.Model):
    rut = models.CharField(max_length=9)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()

def __str__(self):
    return self.nombres, self.apellidos

class Mascota(models.Model):
    foto = models.ImageField()
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50)

def mascota(self):
    return self.nombre  