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

from django.http import Http404

from GestionCouriers.forms.forms import *
from django.urls import reverse

from GestionCouriers.dao.dao_personnePysique import dao_personnePysique
from GestionCouriers.dao.dao_personneMorale import dao_personneMorale
from GestionCouriers.dao.dao_courrier import dao_courrier
from ResourceHumaines.dao.dao_employer import dao_employer
from datetime import datetime, date, timedelta, time
#------------ Time ------------------------
#import datetime
from datetime import datetime, date, timedelta, time
# Create your views here.
# Create your views here.
@login_required(login_url='login_view')
def dashboard(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    print('#### ',dir(username))
    print('entreprise #### ',dir(username.entreprise))
    try:
        context = {'title': 'Dashboard',
                    'entreprise':username.entreprise}
        template = loader.get_template('dashboard.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return printErrorFormat.printError("Views","personneMorale",e,request,"errors/error.html")

@login_required(login_url='login_view')
def profil(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        context = {'title': 'Profil','entreprise':username.entreprise}
        template = loader.get_template('profil.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return printErrorFormat.printError("Views","personneMorale",e,request,"errors/error.html")

@login_required(login_url='login_view')
def personneMorale(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        context = {'title': 'Personne Morale',
                   'entreprise':username.entreprise,
                   'listepersonnep':dao_personneMorale.toListPersonneMorale(username.entreprise,username.entreprise.code)
                   }
        template = loader.get_template('personneMorale.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return printErrorFormat.printError("Views","personneMorale",e,request,"errors/error.html")

@login_required(login_url='login_view')
def postpersonneMorale(request):
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
            intitule=request.POST['intitule']    
            rccm=request.POST['rccm'] 
            siren=request.POST['siren'] 
            Effectifs=request.POST['Effectifs'] 
            Forme_juridique=request.POST['Forme_juridique'] 
            Date_creation_entreprise=request.POST['Date_creation_entreprise'] 
            Date_creation_entreprise = datetime.strptime(str(Date_creation_entreprise), format)
            code_ent=username.entreprise.code
            entreprise=username.entreprise
            utilisateur=username
           
            specialisation=request.POST['specialisation'] 
            adresse=request.POST['adresse'] 
            apropos=request.POST['apropos'] 

            email=request.POST['email'] 
            tel=request.POST['tel'] 
            dao_personneMorale.toSave_or_exists( intitule ,   
            rccm, 
            siren, 
            Effectifs, 
            Date_creation_entreprise, 
            code_ent, 
            entreprise,
            Forme_juridique,
            utilisateur, 
            specialisation, 
            adresse,apropos,email,tel)            

        return HttpResponseRedirect(reverse("personneMorale"))
    except Exception as e:
        print('##### ',e)
        return printErrorFormat.printError("Views","personnePhysique",e,request,"errors/error.html")

@login_required(login_url='login_view')
def postpersonnePhysique(request):
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
            nom=request.POST['nom']    
            postnom=request.POST['postnom'] 
            prenom=request.POST['prenom'] 
            sexe=request.POST['sexe'] 
            age=request.POST['age'] 

            code_ent=username.entreprise.code
            entreprise=username.entreprise
            utilisateur=username
           
            specialisation=request.POST['specialisation'] 
            adresse=request.POST['adresse'] 
            apropos=request.POST['apropos'] 

            email=request.POST['email'] 
            tel=request.POST['tel'] 
            dao_personnePysique.toSave_or_exists( nom ,   
            postnom, 
            prenom, 
            sexe, 
            age, 
            code_ent, 
            entreprise, 
            utilisateur, 
            specialisation, 
            adresse,apropos,email,tel)            

        return HttpResponseRedirect(reverse("personnePhysique"))
    except Exception as e:
        return printErrorFormat.printError("Views","personnePhysique",e,request,"errors/error.html")

@login_required(login_url='login_view')
def personnePhysique(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        context = {'title':'Personne Physique','entreprise':username.entreprise,'listepersonnep':dao_personnePysique.toListPersonnePhysique(username.entreprise,username.entreprise.code)}
        template = loader.get_template('personnePhysique.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return printErrorFormat.printError("Views","personnePhysique",e,request,"errors/error.html")

@login_required(login_url='login_view')
def detailpersonnePhysique(request,codex):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        result=dao_personnePysique.toGetPersonnePhysique(codex,username.entreprise)
        context = {'title':'Détail Personne Physique','entreprise':username.entreprise,'result':result }
        template = loader.get_template('details/detailsPersonneP.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        print("###### ### ",e)
        return printErrorFormat.printError("Views","detailpersonnePhysique",e,request,"errors/error.html")

@login_required(login_url='login_view')
def detailpersonneMorale(request,codex):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        result=dao_personneMorale.toGetPersonneMorale(codex,username.entreprise)
        context = {'title':'Détail Personne Morale','entreprise':username.entreprise,'result':result }
        template = loader.get_template('details/detailsPersonneM.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        print("###### ### ",e)
        return printErrorFormat.printError("Views","detailpersonneMorale",e,request,"errors/error.html")


@login_required(login_url='login_view')
def courrierEntrant(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        listeEmployer=dao_employer.listeEmployer(username.entreprise.code,username.entreprise)
        context = {'title':'Courriers entrants',
                   'entreprise':username.entreprise,
                   'typecourrir':dao_courrier.toListypecourrier(),
                   'nature':dao_courrier.toListNature(),
                   'client_moral':dao_personneMorale.toListPersonneMorale(username.entreprise,username.entreprise.code),
                   'client_physique':dao_personnePysique.toListPersonnePhysique(username.entreprise,username.entreprise.code),
                   'courrier':dao_courrier.toListCourrier(username.entreprise,username.entreprise.code),
                    'listeEmployer':listeEmployer

        }
        template = loader.get_template('courrierEntrant.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return printErrorFormat.printError("Views","personneMorale",e,request,"errors/error.html")

@login_required(login_url='login_view')
def postcourrierEntrant(request):
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
            libele=request.POST['libele']    
            concerne=request.POST['concerne'] 
            reference=request.POST['reference'] 
            typecourrir=request.POST['typecourrir'] 
            nature=request.POST['nature'] 

            code_ent=username.entreprise.code
            entreprise=username.entreprise
            utilisateur=username
           
            client_m=request.POST['client_m'] 
            client_p=request.POST['client_p'] 
            client_intitule=request.POST['client_intitule'] 

            decision=request.POST['decision'] 
            anotation=""

            client_p_exp=request.POST['client_p_exp'] 
            client_m_exp=request.POST['client_m_exp'] 
            client_intitule_exp=request.POST['client_intitule_ex'] 

            dao_courrier.toSave_or_exists( libele ,concerne,reference,typecourrir, 
            nature, 
            code_ent, 
            entreprise, 
            utilisateur, 
            client_m, 
            client_p,client_intitule,decision,anotation,client_p_exp,client_m_exp,client_intitule_exp)            

        return HttpResponseRedirect(reverse("courrierEntrant"))
    except Exception as e:
        print('##### ere',e)
        return printErrorFormat.printError("Views","personnePhysique",e,request,"errors/error.html")


@login_required(login_url='login_view')
def detailCourrier(request,codex):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        result=dao_courrier.toGetCourrier(codex,username.entreprise)
        agents=dao_courrier.toListCourrierAffecte(username.entreprise,username.entreprise.code,result.id)
        print('#### ',agents)
        context = {'title':'Détail Courier','entreprise':username.entreprise,'result':result,
                    'agents':agents
        
        }
        template = loader.get_template('details/detailsCourrrier.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        print("###### ### ",e)
        return printErrorFormat.printError("Views","detailpersonnePhysique",e,request,"errors/error.html")


@login_required(login_url='login_view')
def courrierSortant(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        context = {'title':'Courriers Sortants','entreprise':username.entreprise,
                   'typecourrir':dao_courrier.toListypecourrier(),
                   'nature':dao_courrier.toListNature(),
                   'client_moral':dao_personneMorale.toListPersonneMorale(username.entreprise,username.entreprise.code),
                   'client_physique':dao_personnePysique.toListPersonnePhysique(username.entreprise,username.entreprise.code),
                   'courrier':dao_courrier.toListCourrierSortant(username.entreprise,username.entreprise.code)
        }
        template = loader.get_template('courrierSortant.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return printErrorFormat.printError("Views","personneMorale",e,request,"errors/error.html")


@login_required(login_url='login_view')
def listeCourrier(request):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        context = {'title':'Courriers Classé','entreprise':username.entreprise,
                   'nature':dao_courrier.toListNature(),
                   'client_moral':dao_personneMorale.toListPersonneMorale(username.entreprise,username.entreprise.code),
                   'client_physique':dao_personnePysique.toListPersonnePhysique(username.entreprise,username.entreprise.code),
                   'courrier':dao_courrier.toListCourrierTraiter(username.entreprise,username.entreprise.code)
        }
        template = loader.get_template('listeCourrier.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return printErrorFormat.printError("Views","personneMorale",e,request,"errors/error.html")

@login_required(login_url='login_view')
def detailpersonnePhysique(request,codex):
    #-----------------  user ----------------------
    getuser_id=request.user.id                    #
    username= dao_user.getUtilisateur(getuser_id) #
    #----------------- / user ---------------------
    try:
        result=dao_personnePysique.toGetPersonnePhysique(codex,username.entreprise)
        context = {'title':'Détail Personne Physique','entreprise':username.entreprise,'result':result }
        template = loader.get_template('details/detailsPersonneP.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        print("###### ### ",e)
        return printErrorFormat.printError("Views","detailpersonnePhysique",e,request,"errors/error.html")

@login_required(login_url='login_view')
def postAffectationCourrier(request):
    
    try:
        #-----------------  user ----------------------
        getuser_id=request.user.id                    #
        username= dao_user.getUtilisateur(getuser_id) #
        #----------------- / user ---------------------
        if request.method == 'POST':
            courrier=request.POST['courrier']    
            agent=request.POST['agent']
            codex=request.POST['codex']
       
            entreprise=username.entreprise
            code_ent=username.entreprise.code

            dao_courrier.toAffecterAgent( courrier,agent,entreprise,code_ent)            

        return HttpResponseRedirect(reverse("detailCourrier",args=(codex,)))
    except Exception as e:
        return printErrorFormat.printError("Views","personnePhysique",e,request,"errors/error.html")