from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email= models.EmailField(unique=True, null=True)
    universidad= models.CharField(max_length=20, null=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['universidad']


class Ruta(models.Model):
    lugarSalida = models.CharField(max_length=200)
    lugarLlegada = models.CharField(max_length=200)
    ruta = models.CharField(max_length=200)
    fechaSalida = models.DateTimeField(auto_now=False)
#nombre, universidad, correo, contrasena
