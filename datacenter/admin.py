
from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Model_Utilisateur)
admin.site.register(models.Model_PhotoProfil)

admin.site.register(models.Model_Commune)
 
admin.site.register(models.Entreprise)
admin.site.register(models.Apps)
admin.site.register(models.entrepriseApp)
admin.site.register(models.paiement)