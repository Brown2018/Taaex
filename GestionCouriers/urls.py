"""camus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from GestionCouriers import views
from entrepriseApps import views as  views_


handler404 = views_.handler404
handler500 = views_.handler500
urlpatterns = [
    
    path('index',views.dashboard,name="dashbord"),
    path('profil',views.profil,name="profil"),
    path('personneMorale',views.personneMorale,name="personneMorale"),
    path('personnePhysique',views.personnePhysique,name="personnePhysique"),
    path('courrierEntrant',views.courrierEntrant,name="courrierEntrant"),
    path('courrierSortant',views.courrierSortant,name="courrierSortant"),
    path('listeCourrier',views.listeCourrier,name="listeCourrier"),
    path('listeCourrierAffecter',views.listeCourrierAffecter,name="listeCourrierAffecter"),
    #POST
    path('postpersonneMorale',views.postpersonneMorale,name="postpersonneMorale"),
    path('postpersonnePhysique',views.postpersonnePhysique,name="postpersonnePhysique"),
    path('postpersonneMorale',views.postpersonneMorale,name="postpersonneMorale"),
    path('postcourrierEntrant',views.postcourrierEntrant,name="postcourrierEntrant"),
    path('postAffectationCourrier',views.postAffectationCourrier,name="postAffectationCourrier"),
    path('postAnnotation',views.postAnnotation,name="postAnnotation"),  
    path('postAnnotationCloture',views.postAnnotationCloture,name="postAnnotationCloture"),  
    path('listeCourrierAffecterMesTaches',views.listeCourrierAffecterMesTaches,name="listeCourrierAffecterMesTaches"),
    path('listeCourrierTraiterMesTaches',views.listeCourrierTraiterMesTaches,name="listeCourrierTraiterMesTaches"), 
    re_path(r'^detailperso/(?P<codex>\w+)/$', views.detailpersonnePhysique,name="detailpersonnePhysique"),
    re_path(r'^detailpersmoral/(?P<codex>\w+)/$', views.detailpersonneMorale,name="detailpersonneMorale"),
    re_path(r'^detailCourrier/(?P<codex>\w+)/$', views.detailCourrier,name="detailCourrier"),
    
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
