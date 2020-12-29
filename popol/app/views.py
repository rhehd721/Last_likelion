from django.shortcuts import render, redirect, get_object_or_404
from .models import Popol 

# Create your views here.


# def home(request):
#     popols = Popol.objects.all()
#     return render(request, 'home.html', {'popols': popols})

def intro(request):
    return render(request, 'intro.html')

def About(request):
    return render(request, 'About.html')

def Project(request):
    return render(request, 'Project.html')

def Skill(request):
    return render(request, 'Skill.html')

# def detail(request,popol_id):
#     popols = get_object_or_404(Popol, pk=popol_id)
#     return render(request, 'detail.html', {'popol': popols})