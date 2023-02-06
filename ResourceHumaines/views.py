from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from datacenter.errors.printErrorFormat import printErrorFormat
import os
from security.dao.dao_user import dao_user

from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import Http404

from GestionCouriers.forms.forms import *
from django.urls import reverse

from GestionCouriers.dao.dao_personnePysique import dao_personnePysique
from ResourceHumaines.dao.dao_Fonction import dao_Fonction
from ResourceHumaines.dao.dao_poste import dao_poste
from ResourceHumaines.dao.dao_employer import dao_employer
from datetime import datetime, date, timedelta, time
#------------ Time ------------------------
#import datetime
from datetime import datetime, date, timedelta, time
# Create your views here.
# Create your views here.

@login_required(login_url='login_view')
def listeFonction(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        context = {'title':'Liste de Fonctions','entreprise':username.entreprise,
        'listefonction':dao_Fonction.toListFonction(username.entreprise,username.entreprise.code)}
        template = loader.get_template('listeFonction.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return printErrorFormat.printError("Views","listeFonction",e,request,"errors/error.html")
 
@login_required(login_url='login_view')
def postFonction(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        #-----------------  user ----------------------
        getuser_id=request.user.id                    #
        username= dao_user.getUtilisateur(getuser_id) #
        #----------------- / user ---------------------
        if request.method == 'POST':
            fonction=request.POST['fonction']    
 
            entreprise=username.entreprise
            code_ent=username.entreprise.code

            dao_Fonction.toSave_or_exists( fonction,entreprise,code_ent)            

        return HttpResponseRedirect(reverse("listedefonction"))
    except Exception as e:
        return printErrorFormat.printError("Views","personnePhysique",e,request,"errors/error.html")

@login_required(login_url='login_view')
def listedeposte(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        context = {'title':'Liste de Fonctions','entreprise':username.entreprise,
        'listeposte':dao_poste.toListPoste(username.entreprise,username.entreprise.code),
        'listefonction':dao_Fonction.toListFonction(username.entreprise,username.entreprise.code)}
        template = loader.get_template('listePoste.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return printErrorFormat.printError("Views","listedeposte",e,request,"errors/error.html")
  
@login_required(login_url='login_view')
def postPoste(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        #-----------------  user ----------------------
        getuser_id=request.user.id                    #
        username= dao_user.getUtilisateur(getuser_id) #
        #----------------- / user ---------------------
        if request.method == 'POST':
            fonction=request.POST['fonction']    
            poste=request.POST['poste']
 
            entreprise=username.entreprise
            code_ent=username.entreprise.code

            dao_poste.toSave_or_exists( fonction,poste,entreprise,code_ent)            

        return HttpResponseRedirect(reverse("listedeposte"))
    except Exception as e:
        return printErrorFormat.printError("Views","personnePhysique",e,request,"errors/error.html")
@login_required(login_url='login_view')
def listedepersonnels(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        entreprise=username.entreprise
        listeposte=dao_poste.toListPoste(username.entreprise,username.entreprise.code)
        listefonction=dao_Fonction.toListFonction(username.entreprise,username.entreprise.code)
        listeEmployer=dao_employer.listeEmployer(username.entreprise.code,username.entreprise)
        context = {'title':'Liste de Personnels','entreprise':entreprise,
        'listeposte':listeposte,
        'listefonction':listefonction,
        'listeEmployer':listeEmployer}

        template = loader.get_template('listePersonneles.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        print('## err ',e)
        return printErrorFormat.printError("Views","listedepersonnels",e,request,"errors/error.html")
  
@login_required(login_url='login_view')
def postpersonnels(request):
    
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        #-----------------  user ----------------------
        getuser_id=request.user.id                    #
        username= dao_user.getUtilisateur(getuser_id) #
        #----------------- / user ---------------------
        format = "%Y-%m-%dT%H:%M"
        if request.method == 'POST':
            nom=request.POST['nom']    
            postnom=request.POST['postnom'] 
            prenom=request.POST['prenom'] 
            sexe=request.POST['sexe'] 
            #pays=request.POST['pays'] #

            code_ent=username.entreprise.code
            entreprise=username.entreprise.id
            utilisateur=username
           
            typeuser=request.POST['typeuser'] 
            adresse=request.POST['adresse'] 
            apropos=request.POST['apropos'] 

            email=request.POST['email'] 
            tel=request.POST['tel'] 
            date_naissance=request.POST['date_naissance']
            date_naissance = datetime.strptime(str(date_naissance), format)

            fonction=request.POST['fonction'] 
            poste=request.POST['poste'] 
         
            dao_employer.creationEmployer( nom ,   
            postnom, 
            prenom, 
            utilisateur.id,
            sexe,
            adresse,
            tel,
            entreprise, 
            typeuser,
            date_naissance, 
            code_ent,
            email,
            username.entreprise, apropos,fonction,poste)            

        return HttpResponseRedirect(reverse("listedepersonnels"))
    except Exception as e:
        print('##### error ',e)
        return HttpResponseRedirect(reverse("listedepersonnels"))
