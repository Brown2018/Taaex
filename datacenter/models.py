
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

class Entreprise(models.Model):
    intitule=models.CharField(max_length = 50, null = True, blank = True) 
    Forme_juridique=models.CharField(max_length = 50, null = True, blank = True) #sarl ...
    rccm=models.CharField(max_length = 50, null = True, blank = True) 
    siren=models.CharField(max_length = 150, null = True, blank = True)
    Date_creation_entreprise=models.DateField(null = True, blank = True)
    Effectifs=models.CharField(max_length = 50, null = True, blank = True)
    code=models.CharField(max_length = 150, null = True, blank = True)
    def __str__(self):
        return str(self.intitule)

class entrepriseApp(models.Model):
    entreprise = models.ForeignKey('Entreprise', blank=True, null=True,on_delete=models.CASCADE, related_name="entrepriseApp")
    app = models.ForeignKey('Apps', blank=True, null=True,on_delete=models.CASCADE, related_name="app_r")
    # inscrit, Renvoyer,quiter.
    etat = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return str(self.entreprise)+" "+str(self.app)

class paiement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    entreprise = models.ForeignKey('Entreprise', blank=True, null=True,on_delete=models.CASCADE, related_name="entreprise_paie")
    app = models.ForeignKey('Apps', blank=True, null=True,on_delete=models.CASCADE, related_name="app_paie")
    def __str__(self):
        return str(self.entreprise)

class Apps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    titre = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    background_color = models.CharField(max_length=100, null=True, blank=True)
    background_image = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.titre

class Model_Utilisateur(models.Model):
    entreprise=models.ForeignKey("Entreprise",related_name="mon_entreprise",blank=True, null=True, on_delete=models.CASCADE)
    utilisateur=models.ForeignKey(User,related_name="utilisateur_user" ,blank=True, null=True, on_delete=models.CASCADE)
    utilisateur_esclave=models.ForeignKey("Model_Utilisateur",related_name="model_utilisateur_esclave_user",blank=True, null=True, on_delete=models.CASCADE)
    nom=models.CharField(max_length = 50, null = True, blank = True)    
    postnom=models.CharField(max_length = 50, null = True, blank = True) 
    prenom=models.CharField(max_length = 50, null = True, blank = True) 
    sexe=models.CharField(max_length = 10, null = True, blank = True)
    pays=models.CharField(max_length = 50, null = True, blank = True)
    typeuser=models.CharField(max_length = 50, null = True, blank = True)   
    telephone=models.CharField(max_length = 50, null = True, blank = True)
    date_naissance=models.DateField(null = True, blank = True)
    created=models.DateTimeField(auto_now_add=True)
    adress=models.CharField(max_length = 150, null = True, blank = True)
    code_ent=models.CharField(max_length = 150, null = True, blank = True)
    codex=models.CharField(max_length = 120, null = True, blank = True,unique=True)
    apropos=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return str(self.utilisateur)


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

class Model_Usser_Allow(models.Model):
    user = models.ForeignKey(Model_Utilisateur,related_name="user_allow", blank=True, null=True, on_delete=models.CASCADE)
    codeSecret=models.CharField(max_length = 150, null = True, blank = True)
    def __str__(self):
        return str(self.codeSecret)

class Model_Moi(models.Model):
    email=models.CharField(max_length = 150, null = True, blank = True)
    e=models.CharField(max_length = 150, null = True, blank = True)