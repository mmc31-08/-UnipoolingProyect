
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from matplotlib.style import context
from .models import Ruta, User
from .forms import RutaForm, MyUserCreationForm


def home(request):
    return render(request, 'home.html')


def principal(request): 
    return render(request, 'principal.html')


def register(request):
    form = MyUserCreationForm()
    if request.method=='POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username= user.username.lower()
            user.save()            
            return redirect('principal')
        else: 
            messages.error(request, 'An error occurred during registration')
    
    return render(request,'register.html', { 'form' : form})

def rutas(request):
    ruta = Ruta.objects.all()
    context = {'rutas': ruta}
    return render(request, 'ruta.html', context)


def registrarRutaView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(Ruta, id=pk)
        if request.method == 'POST':
            formr = RutaForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                formr = RutaForm(request.POST)
                if formr.is_valid():
                    formr.save()
                    return redirect('/rutas/') 
                else:
                    messages.error(request, formr.errors)
        else:
            formr = RutaForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            formr = RutaForm(request.POST)
            if formr.is_valid():
                formr.save()
                return redirect('/rutas/') 
            else:
                messages.error(request, formr.errors)
    else:
        formr = RutaForm()

    context = {'formr': formr, 'disabled': (kwargs.get('pk', None) != None), 'nombre_modelo': 'Ruta'}

    return render(request, 'registrarRuta.html', context) #cambia
