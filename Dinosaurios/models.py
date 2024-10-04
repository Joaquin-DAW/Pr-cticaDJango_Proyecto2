from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
    
class Dinosaurio(models.Model):
    nombre = models.CharField(max_length=100)
    era = models.CharField(max_length=150)
    dieta = models.CharField(max_length=100)

class Paleontologo(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    anos_experiencia = models.IntegerField()

class Excavacion(models.Model):
    ubicacion = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)
    dinosaurio = models.ForeignKey(Dinosaurio, on_delete=models.CASCADE)