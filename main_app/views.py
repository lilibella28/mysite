from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'projects.html')

def contacts(request):
    return render(request, 'contacts.html')



    # Views are the controllorer in Django
    # Django file path, not request, everything is handle inside the views
    # find the matching end point in certain app. 
    # There is a lot of code that we did not write. 

    # Django is different that express, have allow of building in functionality
    # Django have helpers classess, methods

    