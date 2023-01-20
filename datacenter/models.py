
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.
 
class Model_Utilisateur(models.Model):
    utilisateur=models.ForeignKey(User,related_name="utilisateur_user" ,blank=True, null=True, on_delete=models.CASCADE)
    utilisateur_esclave=models.ForeignKey("Model_Utilisateur",related_name="model_utilisateur_esclave_user",blank=True, null=True, on_delete=models.CASCADE)
    sexe=models.CharField(max_length = 10, null = True, blank = True)
    pays=models.CharField(max_length = 50, null = True, blank = True)

    typeuser=models.CharField(max_length = 50, null = True, blank = True)   
    telephone=models.CharField(max_length = 50, null = True, blank = True)
    date_naissance=models.DateField(null = True, blank = True)
    
    created=models.DateTimeField(auto_now_add=True)
    adress=models.CharField(max_length = 150, null = True, blank = True)
    
    def __str__(self):
        return str(self.utilisateur.username)

class Model_PhotoProfil(models.Model):
    auteur=models.ForeignKey("Model_Utilisateur", related_name="utilisateur_photo",blank=True, null=True, on_delete=models.CASCADE)
    avatar=models.CharField(max_length = 150, null = True, blank = True)
    shortpath=models.CharField(max_length = 150, null = True, blank = True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.avatar


class Model_Commune(models.Model):
    designation=models.CharField(max_length = 150, null = True, blank = True)
    Superficie=models.CharField(max_length = 150, null = True, blank = True) #km^2
    description=models.TextField()
    localsation=models.CharField(max_length = 150, null = True, blank = True)
   
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.designation

class Model_parametreSuplementaireProduit(models.Model):
    parametre=models.CharField(max_length = 150, unique=True, null = True, blank = True)
    def __str__(self):
        return self.parametre


class Model_valeurParametreeSuplementaireProduit(models.Model):
    valeur=models.CharField(max_length = 150, unique=True, null = True, blank = True)
    def __str__(self):
        return str(self.valeur)
