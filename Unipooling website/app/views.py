from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import MyUserCreationForm


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
