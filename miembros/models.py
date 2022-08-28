from django.db import models

# Create your models here.
"""nombre y parentezco"""

class Familiares(models.Model):
    nombre = models.CharField(max_length=128)
    fecha_nacimiento=models.DateField()
    peso = models.IntegerField()

# nombre

class Parentezco(models.Model):
   nombre = models.CharField(max_length=128)
   familiares_project = models.ForeignKey('Familiares', on_delete=models.CASCADE, null=True)


    


