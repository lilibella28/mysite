from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    technology = models.CharField(max_length=100)
    link = models.CharField(max_length=100)