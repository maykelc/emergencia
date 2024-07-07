from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    
    
class Alerta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    

class ubicacion(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Lat:{self.latitude}, Long:{self.longitude}'