
from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Model_Employer)
admin.site.register(models.Model_Employer_Fonction)
admin.site.register(models.Model_Postes_Fonction)
admin.site.register(models.Model_Employer_Fonction_Poste)