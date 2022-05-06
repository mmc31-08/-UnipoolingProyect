
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from .forms import RutaForm, MyUserCreationForm, vehiculoForm


def home(request):
    return render(request, 'home.html')


def principal(request): 
    return render(request, 'principal.html')


def horario(request): 
    context = {
        "horarios" : User.objects.all()
    }
    return render(request, 'horario.html', context)


def vehiculo(request): 
        if request.method == 'POST':
            formr = vehiculoForm(request.POST)
            if formr.is_valid():
                formr.instance.user = request.user
                formr.save()
                messages.success(request, 'Se ha registrado tu vehiculo')
                return redirect('principal') 
            else:
                messages.success(request, 'Verifica tus datos')
        else:
            formr =vehiculoForm()

        return render(request, 'vehiculoh.html', context={"formr": formr}) #cambia


def datos(request):
    return render(request, 'datos.html')

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

    return render(request, 'registrarRuta.html', context) 

def datosVehiculo(request):
    logged_in_user_vehiculo = Vehiculo.objects.filter(user_id=8)
    return render(request, 'datosVehiculo.html', {'vehiculo': logged_in_user_vehiculo})
 