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
        return self.nom
        
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


class Model_TypeCourrier(models.Model):
    typecourrir=models.CharField(max_length = 150, null = True, blank = True)
    def __str__(self) -> str:
        return self.typecourrir
        
class Model_NatureCourrier(models.Model):
    nature=models.CharField(max_length = 150, null = True, blank = True)

    def __str__(self) -> str:
        return self.nature
        

class Model_courrier(models.Model):
    code_ent=models.CharField(max_length = 150, null = True, blank = True)
    entreprise=models.ForeignKey(Entreprise, blank=True, null=True, on_delete=models.CASCADE)
    codex=models.CharField(max_length = 120, null = True, blank = True,unique=True)
    libele=models.CharField(max_length = 50, null = True, blank = True) 
    Date_arriver=models.DateField(auto_now_add=True)
    Date_traitement=models.DateField(auto_now=True, null = True, blank = True)
    decision=models.TextField( null = True, blank = True) #Commentaire
    concerne=models.CharField(max_length = 150, null = True, blank = True) 
    reference=models.CharField(max_length = 150, null = True, blank = True)
    typecourrir=models.ForeignKey("Model_TypeCourrier", blank=True, null=True, on_delete=models.CASCADE)

    nature=models.ForeignKey("Model_NatureCourrier", blank=True, null=True, on_delete=models.CASCADE)

    client_p=models.ForeignKey("Model_PersonnePhysique", blank=True, null=True, on_delete=models.CASCADE)
    client_m=models.ForeignKey("Model_PersonneMorale", blank=True, null=True, on_delete=models.CASCADE)
    client_intitule=models.CharField(max_length = 150, null = True, blank = True)

    client_p_exp=models.ForeignKey("Model_PersonnePhysique",related_name="client_p_exp", blank=True, null=True, on_delete=models.CASCADE)
    client_m_exp=models.ForeignKey("Model_PersonneMorale",related_name="client_m_exp", blank=True, null=True, on_delete=models.CASCADE)
    client_intitule_exp=models.CharField(max_length = 150, null = True, blank = True)
    
    traiter=models.BooleanField(default=False)
    consulter=models.BooleanField(default=False)
    afecter=models.BooleanField(default=False)
    utilisateur=models.ForeignKey(Model_Utilisateur, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.libele
class Model_Annotation(models.Model):
    courrier=models.ForeignKey("Model_courrier",related_name="mes_annotation", blank=True, null=True, on_delete=models.CASCADE)# tab
    code_ent=models.CharField(max_length = 150, null = True, blank = True)
    entreprise=models.ForeignKey(Entreprise,related_name="mes_courriers",blank=True, null=True, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    annotation=models.TextField(blank=True,null=True)
    employer=models.ForeignKey(Model_Utilisateur,related_name="mes_annitations",blank=True, null=True, on_delete=models.CASCADE)
    codex=models.CharField(max_length = 120, null = True, blank = True,unique=True)
    def __str__(self):
        return str(self.annotation)
  
class Model_AgentAffecterCourrier(models.Model):
    code_ent=models.CharField(max_length = 150, null = True, blank = True)
    entreprise=models.ForeignKey(Entreprise,related_name="affectercourrier_entreprise",blank=True, null=True, on_delete=models.CASCADE)
    agent=models.ForeignKey(Model_Utilisateur,related_name="agent_courrier",blank=True, null=True, on_delete=models.CASCADE)
    courrier=models.ForeignKey("Model_courrier",related_name="courrier",blank=True, null=True, on_delete=models.CASCADE)
    codex=models.CharField(max_length = 120, null = True, blank = True,unique=True)
    def __str__(self):
        return str(self.courrier)

