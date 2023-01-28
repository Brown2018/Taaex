from django.db import models
from django.conf import settings
from django.db import models
from .storage.storages import Storages
from datacenter.models import Model_Utilisateur,Entreprise


def select_storage():
    return Storages.MyLocalStorage() if settings.DEBUG else Storages.MyRemoteStorage()


class Model_Client(models.Model):
    code_ent=models.CharField(max_length = 150, null = True, blank = True)
    entreprise=models.ForeignKey(Entreprise, blank=True, null=True, on_delete=models.CASCADE)
    utilisateur=models.ForeignKey(Model_Utilisateur, blank=True, null=True, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)
    
    specialisation=models.CharField(max_length = 50, null = True, blank = True) 
    adresse=models.CharField(max_length = 50, null = True, blank = True)
    apropos=models.TextField(null=True,blank=True) 
    telephone=models.CharField(max_length = 50, null = True, blank = True)
    email=models.CharField(max_length = 50, null = True, blank = True)
    codex=models.CharField(max_length = 120, null = True, blank = True,unique=True)
   

class Model_PersonnePhysique(Model_Client):
    nom=models.CharField(max_length = 50, null = True, blank = True)    
    postnom=models.CharField(max_length = 50, null = True, blank = True) 
    prenom=models.CharField(max_length = 50, null = True, blank = True) 
    sexe=models.CharField(max_length = 50, null = True, blank = True) 
    age=models.IntegerField( null = True, blank = True) 
    
    def __str__(self) -> str:
        return super().__str__()
        
class Model_dossiers_pp(models.Model):
    personnep=models.ForeignKey(Model_PersonnePhysique,related_name="mes_fichiers_pp", blank=True, null=True, on_delete=models.CASCADE)
    fichier_pp = models.FileField(storage=select_storage,null = True, blank = True)    


#Entreprise
class Model_PersonneMorale(Model_Client):
    intitule=models.CharField(max_length = 50, null = True, blank = True) 
    Forme_juridique=models.CharField(max_length = 50, null = True, blank = True) #sarl ...
    rccm=models.CharField(max_length = 50, null = True, blank = True) 
    siren=models.CharField(max_length = 150, null = True, blank = True)
    Date_creation_entreprise=models.DateField(null = True, blank = True)
    Effectifs=models.CharField(max_length = 150, null = True, blank = True)


class Model_dossiers_pm(models.Model):
    personnem=models.ForeignKey(Model_PersonneMorale,related_name="mes_fichiers_pm", blank=True, null=True, on_delete=models.CASCADE)
    fichier_pm = models.FileField(storage=select_storage,null = True, blank = True)    
