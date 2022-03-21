from django.db import models


class usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    universidad=models.CharField(max_length=20)
    correo=models.EmailField()
    contraseña=models.CharField(max_length=15)  

#nombre, universidad, correo, contrasena

