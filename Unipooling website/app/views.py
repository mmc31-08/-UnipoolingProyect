from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def principal(request): 
    return render(request, 'principal.html')