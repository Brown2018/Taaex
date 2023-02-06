# -*- coding: utf-8 -*-
from datacenter.models import Model_Utilisateur
from datetime import datetime, date, timedelta, time
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.sessions.models import Session
from django.utils import timezone
import datetime
from ResourceHumaines.models import Model_Employer,Model_Employer_Fonction_Poste
import secrets
import string
from security.mails.dao_sendMailConfirmationCount import dao_sendMailConfirmationCount
from ResourceHumaines.models import Model_Employer
from datacenter.models import Model_Utilisateur,Model_Moi
class dao_employer(object):

    @staticmethod
    def listeEmployer(code_ent,entreprise):
        try:
            employ=  Model_Utilisateur.objects.filter(code_ent=code_ent,entreprise=entreprise).select_related('utilisateur','utilisateur_esclave','entreprise')    
            return employ
            
        except Exception as e:
            print("IL Y A PAS D'UTILISATEUR AVEC CETTE IDENTIFIANT  Backend((getUtilisateur)) err=",e)

    @staticmethod
    def creationEmployer(nom,postnom,prenom, userMaster,sexe,adresse,tel,entreprise,typeuser,date_naissance,code_ent,email,entreprise_n,apropos,fonction,poste):
        
        user = User()
        utilisateurUser = Model_Utilisateur()
        fp=Model_Employer_Fonction_Poste()
        try:
            codex=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(100))
            passworw=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(10))
            user.username = email.strip()
            user.email = email
            user.set_password(passworw)
            #on verrifie

            utilisateurUser.nom=nom
            utilisateurUser.postnom=postnom
            utilisateurUser.prenom=prenom
            utilisateurUser.sexe=sexe
           
            utilisateurUser.adress=adresse
            utilisateurUser.telephone=tel
            utilisateurUser.entreprise_id=entreprise #
            utilisateurUser.typeuser=typeuser
            utilisateurUser.date_naissance=date_naissance
            utilisateurUser.codex=codex,
            utilisateurUser.code_ent=code_ent
            utilisateurUser.apropos=apropos
            
            
            utilisateurUser.utilisateur_esclave_id=userMaster
            User.objects.get(email=email)
        except Exception as e:
            try:
                user.save()
                moi=Model_Moi()
                moi.email=user.username
                moi.e=passworw
                moi.save()
                utilisateurUser.utilisateur_id=user.id
                utilisateurUser.save()
                fp.employer_id=utilisateurUser.id
                fp.fonction_id=fonction
                fp.poste_id=poste
                fp.save()
                message=dao_sendMailConfirmationCount.sendMailCoordonnes(email,passworw,entreprise_n,email)
                print(" MESSAGE ",message)               
            except Exception as e:
                print("PROBLEME DE CREATION D'UTILISATEUR AVEC CETTE IDENTIFIANT  Backend(dao_menu(creationVendeur)) err=",e)

 
    @staticmethod
    def updateUtilisateur(id,user,sexe,date,pays,adresse,tel):
        try:
        
            utilisateurUser = Model_Utilisateur.objects.select_related('utilisateur').get(pk=id)
            utilisateurUser.utilisateur=user
            utilisateurUser.sexe=sexe
            utilisateurUser.pays=pays
            utilisateurUser.adress=adresse
            utilisateurUser.telephone=tel
            utilisateurUser.date_naissance=date           
           
            utilisateurUser.save()
        except Exception as e:
            print("PROBLEME DE CREATION D'UTILISATEUR AVEC CETTE IDENTIFIANT  Backend(dao(updateUtilisateur)) err=",e)

    @staticmethod
    def updateFirstLastName(id,fisrtname,lastname):
        try:

            user = User.objects.get(username=id)
            user.first_name=fisrtname
            user.last_name=lastname       
            user.save()
        except Exception as e:
            print("PROBLEME DE CREATION D'UTILISATEUR AVEC CETTE IDENTIFIANT  Backend(dao(updateFirstLastName)) err=",e)

    @staticmethod
    def create_or_updateIdentity(id,auteur,profession,domain_expertise,niveau_etude,description,champInterret,cite_web):
        try:
            #print('ID dans Dao user ',id)
            if id != 0:
                identite=Model_Identite.objects.select_related('auteur__utilisateur').get(pk=id)
            else :
                identite=Model_Identite()
            identite.auteur=auteur
            identite.profession=profession
            identite.domain_expertise=domain_expertise
            identite.niveau_etude=niveau_etude
            identite.description=description
            identite.champInterret=champInterret
            identite.cite_web=cite_web
            identite.save()

        except Exception as e:
            print("PROBLEME DE CREATION D'UTILISATEUR AVEC CETTE IDENTIFIANT  Backend(dao(create_or_updateIdentity) err=",e)
    
    @staticmethod
    def getMembersByGender(auteur,gender):
        # HERE
        try:
            container=[]
            usernames=[]
            #For people
            #la valeur ajouté 1 n'a rien avoir avec le contex
            if gender==1:
                data= Model_Utilisateur.objects.all().select_related('utilisateur').exclude(utilisateur__username=auteur).exclude(utilisateur__is_active=False).order_by('-id')
                for user in data:
                    usernames.append(user.utilisateur.username)
                #Elimination de doublons
                usernames=set(usernames)
                usernames=list(usernames)
                #/ Verification doublon
                try:
                    # On exclu les contacts
                    for contact in Model_contact.objects.select_related('auteur__utilisateur').filter(auteur=auteur):
                        for user in usernames:
                            if contact.contactUsername==user:
                                usernames.remove(contact.contactUsername)
                except Exception:
                    usernames
                for item in usernames:
                    data= Model_Utilisateur.objects.select_related('utilisateur').filter(utilisateur__username=item).exclude(utilisateur__username=auteur).exclude(utilisateur__is_active=False).order_by('-id')
                    container.append(data)
                return container
            # for Entreprise and Start-up
        except Exception as e:
            print('getMembersByGender err=',e)

    @staticmethod
    def getByResearchMembersByUsernameAndFirst(auteur,query):
        try:
            
            #this list will contains all unique username by set functioon 
            username=[]
            usernamed=[]
            #getting user from services
            datafromService= Model_Service.objects.select_related('auteur__utilisateur').filter(Q(service__contains=query)).exclude(auteur__utilisateur__username=auteur)
            #getting user from skills
            datafromSkills= Model_Competence.objects.select_related('auteur__utilisateur').filter(Q(skils__contains=query)).exclude(auteur__utilisateur__username=auteur)
            #getting user from utilisateur
            data= Model_Utilisateur.objects.select_related('utilisateur').filter(Q(utilisateur__username__contains=query) |Q(utilisateur__first_name__contains=query)).exclude(utilisateur__username=auteur)
            #getting by identity
            dataIdentity=Model_Identite.objects.select_related('auteur__utilisateur').filter(Q(profession__contains=query))

            for fromskill in datafromSkills:
                username.append(fromskill.auteur.utilisateur.username)
            for fromuser in data:
                username.append(fromuser.utilisateur.username)
            for fromservices in datafromService:
                username.append(fromservices.auteur.utilisateur.username)
            for identeite in dataIdentity:
                username.append(identeite.auteur.utilisateur.username)
            #Elimination de doublons
            username=set(username)
            username=list(username)
            #/ Verification doublon

            try:
                #on exclu tout nos contact
                for contact in Model_contact.objects.select_related('auteur__utilisateur').filter(auteur=auteur):
                    for user in username:
                        if contact.contactUsername==user:
                            username.remove(contact.contactUsername)
            except Exception:
                #En cas d'exception, c.a.d pas encore de contacts on remet les resultats de la recherche.
                username
            
            for usern in username:
                Fromdatatosend= Model_Utilisateur.objects.select_related('utilisateur').filter(utilisateur__username__contains=usern).exclude(utilisateur__username=auteur)
                usernamed.append(Fromdatatosend)
            return usernamed
        except Exception as e:
            print('getMembersByGender err=',e)


    @staticmethod
    def AllUsers():
        try:
            return Model_Utilisateur.objects.all().select_related('utilisateur').count()
        except Exception as e:
            print('listMyContacts err=',e)
    
    # recuperer les utilisateur connectés
    @staticmethod
    def get_current_users():
        active_sessions = Session.objects.select_related().filter(expire_date__gte=timezone.now())
        user_id_list = []
        for session in active_sessions:
            data = session.get_decoded()
            user_id_list.append(data.get('_auth_user_id', None))
        # Query all logged in users based on id list
        return User.objects.filter(id__in=user_id_list)