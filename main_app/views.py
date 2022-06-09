from django.shortcuts import render
from .models import Project
# Create your views here.
from django.http import HttpResponse

def projects_index(request):
    projects = Project.description
    return(request, 'projects.html', {'projects': projects})

def home(request):
    return render(request, 'home.html')

def skill(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'projects.html')

def contacts(request):
    return render(request, 'contacts.html')

def experience(request):
    return render(request, 'experience.html')

    # Views are the controllorer in Django
    # Django file path, not request, everything is handle inside the views
    # find the matching end point in certain app. 
    # There is a lot of code that we did not write. 

    # Django is different that express, have allow of building in functionality
    # Django have helpers classess, methods

    