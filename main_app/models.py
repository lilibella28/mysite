from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField
    description = models.TextField
    technology = models.CharField
    link = models.CharField