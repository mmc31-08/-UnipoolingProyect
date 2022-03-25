from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email= models.EmailField(unique=True, null=True)
    universidad= models.CharField(max_length=20, null=True)
    horario = models.ImageField(upload_to = 'static/images/', blank=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['universidad', 'horario']


class Ruta(models.Model):
    lugarSalida = models.CharField(max_length=200)
    lugarLlegada = models.CharField(max_length=200)
    ruta = models.CharField(max_length=200)
    fechaSalida = models.DateTimeField(auto_now=False)

class Vehiculo(models.Model):
    placa = models.CharField(max_length=6, validators=[MinLengthValidator(6)],blank=False, null=False)
    color = models.CharField(max_length=10)
    modelo = models.CharField(max_length=200)

