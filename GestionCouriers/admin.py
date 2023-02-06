from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Model_PersonneMorale)
admin.site.register(models.Model_PersonnePhysique)
admin.site.register(models.Model_TypeCourrier)
admin.site.register(models.Model_courrier)
admin.site.register(models.Model_NatureCourrier)
admin.site.register(models.Model_AgentAffecterCourrier)