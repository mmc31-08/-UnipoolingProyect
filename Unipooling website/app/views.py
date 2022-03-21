from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def principal(request): 
    return render(request, 'principal.html')


def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            messages.success(request, f'usuario {username} creado')
            return redirect('principal')
    else: 
        form=UserRegisterForm()
    
    context= { 'form' : form}
    return render(request,'register.html', context)