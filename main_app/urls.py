from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skill/', views.skill, name='skill'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
    path('experience/', views.experience, name="experience")
    
]