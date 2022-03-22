from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email= models.EmailField(unique=True, null=True)
    universidad= models.CharField(max_length=20, null=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['unviersdidad']

#nombre, universidad, correo, contrasena
