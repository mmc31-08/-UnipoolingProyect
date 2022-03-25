from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'universidad', 'horario']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', ]


class RutaForm(ModelForm):
    class Meta:
        model = Ruta

        fields = '__all__'

        widgets = {
            'lugarSalida': forms.TextInput(attrs={'class': 'form-control'}),
            'lugarLlegada': forms.TextInput(attrs={'class': 'form-control'}),
            'ruta': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaSalida': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
