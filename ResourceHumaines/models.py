
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.
from datacenter.models import Model_Utilisateur
from GestionCouriers.models import Entreprise


class Model_Employer_Fonction(models.Model):
    code_ent=models.CharField(max_length = 150, null = True, blank = True)
    entreprise=models.ForeignKey(Entreprise,related_name="fonction_entreprise",blank=True, null=True, on_delete=models.CASCADE)
    fonction=models.CharField(max_length = 10, null = True, blank = True)
    codex=models.CharField(max_length = 120, null = True, blank = True,unique=True)
    created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.fonction)

class Model_Postes_Fonction(models.Model):
    code_ent=models.CharField(max_length = 150, null = True, blank = True)
    entreprise=models.ForeignKey(Entreprise,related_name="poste_entreprise",blank=True, null=True, on_delete=models.CASCADE)
    fonction=models.ForeignKey("Model_Employer_Fonction",related_name="mon_poste",blank=True, null=True, on_delete=models.CASCADE)
    poste=models.CharField(max_length = 10, null = True, blank = True)
    codex=models.CharField(max_length = 120, null = True, blank = True,unique=True)
    def __str__(self):
        return str(self.poste)


class Model_Employer(Model_Utilisateur):
    date_engagement=models.DateField(null = True, blank = True)
    def __str__(self):
        return str(self.date_engagement)

class Model_Employer_Fonction_Poste(models.Model):
    employer=models.ForeignKey(Model_Utilisateur,related_name="employer_fonction_poste",blank=True, null=True, on_delete=models.CASCADE)
    fonction=models.ForeignKey("Model_Employer_Fonction",related_name="mon_fonction",blank=True, null=True, on_delete=models.CASCADE)
    poste=models.ForeignKey("Model_Postes_Fonction",related_name="mon_poste",blank=True, null=True, on_delete=models.CASCADE)
    date_engagement=models.DateField(null = True, blank = True)
    def __str__(self):
        return str(self.date_engagement)

class Model_Observation(models.Model):
    code_ent=models.CharField(max_length = 150, null = True, blank = True)
    entreprise=models.ForeignKey(Entreprise,related_name="observqtion_entreprise",blank=True, null=True, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    observation=models.TextField(blank=True,null=True)
    employer=models.ForeignKey(Model_Utilisateur,related_name="mon_entreprise",blank=True, null=True, on_delete=models.CASCADE)
    codex=models.CharField(max_length = 120, null = True, blank = True,unique=True)
    def __str__(self):
        return str(self.observation)
