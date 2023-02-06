from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth import (authenticate,get_user_model,login,logout)
from django.contrib.auth.models import User,Group
from django.urls import reverse_lazy, reverse
import datetime
from random import randint
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .mails.dao_sendMailConfirmationCount import dao_sendMailConfirmationCount

from django.conf import settings
from django.utils import timezone
from .dao.dao_user import dao_user

#-----------------  Menu -------------------------------
#from profil.TkngoGestionMenu.tkngoMenu import tkngoMenu
#-------------------------------------------------------

def signIn(request):
    try:

        next = request.GET.get('next')
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        login(request,user)
        if user.is_authenticated:
            #-----------------  user ----------------------
            getuser_id=user.id                    #
            username= dao_user.getUtilisateur(getuser_id) #
            #----------------- / user ---------------------            
        else:
            raise Exception

        dash_board = 'Enregistrement'
        context = {
            'title': "Dashboard",
            'entreprise':username.entreprise
            #'application':menu
        }
        # template = loader.get_template('aSideTop/Layout.html')
        #return HttpResponseRedirect(reverse('index'))
        template = loader.get_template('index.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        print(" PROBLEME ",e)
        context = {
            'error':"Soit le Nom d'utilisateur ou le mot de passe est incorrecte "+str(e),
            'titreH3':"Connectez vous, Please!!!"}
        template = loader.get_template('Security/sign-in.html')
        return HttpResponse(template.render(context, request))


def logout_view(request):
    logout(request)
    context = {'login': 'login'}
    template = loader.get_template('Security/sign-in.html')
    return HttpResponse(template.render(context, request))

def iam_authenticated(request):
    try:
        if request.user.is_authenticated:
            return None
        else:
            context = {'login': 'login'}
            template = loader.get_template('Security/login.html')
            return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {'login': 'login',
                   'erreur':e
        }
        template = loader.get_template('Security/login.html')
        return HttpResponse(template.render(context, request))

@transaction.atomic
def creer_un_user(request):
    try:
        user = User()
        #next = request.GET.get('next')
        usernameForm=request.POST['username']
        user.username = usernameForm.strip()
        #user.first_name = request.POST['first_name']
        #user.last_name = request.POST['last_name']
        email= request.POST['email']
        user.email = email
        password = request.POST['password']

        sexe = request.POST['sexe']
        date= str(request.POST['date']) 
        print('DATE : ',date)
       
        date=datetime.datetime.strptime(date,"%Y-%m-%d")
       
        pays= request.POST['pays']
        adresse=request.POST['adress']
        tel=request.POST['tel']
        user.is_active=False
        user.set_password(password)
        #verification du email

        #on verifie si l'utilisateur existe
        try:
            User.objects.get(username=usernameForm)
            User.objects.get(email=email)

            context = {
            'error': "Veuillez compléter correctement les champs « nom d\'utilisateur » et « mot de passe » d\'un compte autorisé. Sachez que les deux champs peuvent être sensibles à la casse. \n Vous pouvez ",
            'titreH3':"Connectez vous, Please!!!"}
            template = loader.get_template('Security/sign-in.html')
            return HttpResponse(template.render(context, request))
        except User.DoesNotExist:
            user.save()
            dao_user.creationUtilisateur(user,sexe,date,pays,adresse,tel)
            #user = authenticate(username=user.username, password=password)
            message=dao_sendMailConfirmationCount.sendMaimConfCount(user.id,email)
            
            context = {
                'message':message ,
                'email': email,
                'user':user
            }
           
            template = loader.get_template('Security/receiveMail.html')
            return HttpResponse(template.render(context, request))

    except Exception as e:
        context = {'error': "Veuillez compléter correctement les champs « nom d\'utilisateur » et « mot de passe » d\'un compte autorisé. Sachez que les deux champs peuvent être sensibles à la casse. ou soit email et username existe déjà"+str(e),
         'titreH3':"Connectez vous, Please!!!"}
        template = loader.get_template('Security/sign-in.html')
        return HttpResponse(template.render(context, request))

def resentMessage(request):
    try:
        email= request.POST['email']
        user= request.POST['user']

        message=dao_sendMailConfirmationCount.sendMaimConfCount(user,email)
        context = {
                'message':message ,
        }
           
        template = loader.get_template('Security/receiveMail.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {
                'message':e ,
        }
           
        template = loader.get_template('Security/MessageRecive.html')
        return HttpResponse(template.render(context, request))
        
def activationUser(request):

    try:
        user=request.GET['user']
        getUser = User.objects.get(id=user)
        getUser.is_active=True
        getUser.save()
        context = {'login': 'login',
                    'error':"",
                    'titreH3':"Connectez vous, Please!!!"}
        template = loader.get_template('Security/sign-in.html')
        return HttpResponse(template.render(context, request))

    except Exception as e:
        context = {'login': 'login',  
                   'error':e,
                    'titreH3':"Connectez vous, Please!!!"
        }
        template = loader.get_template('Security/signin.html')
        return HttpResponse(template.render(context, request))


def get_Username(request):
    try:
        if request.method == 'GET':
            username=request.GET['username']
            #email=request.GET['email']
            result=User.objects.get(username=username)
            if result:
                return JsonResponse("true", safe=False)
            
    except User.DoesNotExist:
        return JsonResponse("false", safe=False)

def returnMailByUSername(request):
    try:
        donnee=[]
        value=""
        username=request.GET['username']
        result=User.objects.get(username=username)
        
        
        if len(result.email) > 0:
            value=result.email
            data={
                'email':value[:3]
            }
            donnee.append(data)
        else:
            return JsonResponse({"val":0}, safe=False)               
        return JsonResponse(donnee, safe=False)
    except User.DoesNotExist:
        return JsonResponse({"val":0}, safe=False)

def returnMailByUSernameChecking(request):
    try:
        donnee=[]
        username=request.GET['username']
        email=request.GET['email']

        result=User.objects.get(username=username)
    
        if result.email == email:
            data={
                'true':"true"
            }
            donnee.append(data)
        else:
            data={
                'true':"false"
            }
            donnee.append(data)
            return JsonResponse(donnee, safe=False)             
        return JsonResponse(donnee, safe=False)
    except User.DoesNotExist:
        return JsonResponse({"true":"false"}, safe=False)

def InitializationBySendingMail(request):
    try:

        donnee=[]
        username=request.GET['username']
        email=request.GET['email']

        result=User.objects.get(username=username)
        randomId = randint(0, 2340)
        password="Tklog"+ str(randomId) +"@changethis"
        result.set_password(password)
        result.save()
        print('',password)
        if result.email == email:
            message=dao_sendMailConfirmationCount.sendingMail(password,result.email)
            data={
                'message':message
            }
            donnee.append(data)
        else:
            data={
                'message':"error check  your e-mail or username ,Please !!!"
            }
            donnee.append(data)
            return JsonResponse(donnee, safe=False)             
        return JsonResponse(donnee, safe=False)
    except Exception :
        return JsonResponse({"message":"error check your e-mail or username ,Please !!!"}, safe=False)

def get_Useremail(request):
    try:
        email=request.GET['email']
        result=User.objects.get(email=email)
        if result:
            return JsonResponse("true", safe=False)
        
    except User.DoesNotExist:
        return JsonResponse("false", safe=False)

def changePPassWord(request):
    try:
        password=request.POST["password"]
        password1=request.POST["confirm"]
        #----------- GET USER ---------------
        if password == password1:
            getuser_id=request.user
            if getuser_id.pk:
                orig_obj = User.objects.get(pk=getuser_id.pk)

                if password1 != orig_obj.password:
                    getuser_id.set_password(password1)
                else:
                    getuser_id.set_password(orig_obj.password)
                getuser_id.save()
        else:
            raise Exception

        return HttpResponseRedirect(reverse('login_view'))
    except Exception :
        return HttpResponseRedirect(reverse('login_view'))

def changeUsername(request):
   
    try:
        username=request.POST["username"]
        #----------- GET USER ---------------
        getuser_id=request.user
        if getuser_id.pk:
           orig_obj = User.objects.get(pk=getuser_id.pk)

           if username != orig_obj.username:
                orig_obj.username=username
                orig_obj.save()
        else:
            raise Exception

        return HttpResponseRedirect(reverse('ModuleClientCount_settingProfil'))
    except Exception :
        return HttpResponseRedirect(reverse('login_view'))

def changeEmail(request):
    try:
        email=request.POST["email"]
        #----------- GET USER ---------------
        getuser_id=request.user
        if getuser_id.pk:
           orig_obj = User.objects.get(pk=getuser_id.pk)

           if email != orig_obj.email:
                orig_obj.email=email
                orig_obj.save()
        else:
            raise Exception

        return HttpResponseRedirect(reverse('ModuleClientCount_settingProfil'))
    except Exception :
        return HttpResponseRedirect(reverse('login_view'))

def ReachRecupererPassword(request):
    logout(request)
    context = {'restorePassword': 'login'}
    template = loader.get_template('Security/recuperationPaswword.html')
    return HttpResponse(template.render(context, request))
    
@login_required(login_url='login_view')
def jointUs(request):
    context = {'contact': 'us'}
    template = loader.get_template('ContactUs/JoinUS.html')
    return HttpResponse(template.render(context, request))

#----------------------------------------------------------------------------------------------------------
#                 --GET--
#----------------------------------------------------------------------------------------------------------

def get_sign_in(request):
    context = {'title': 'Connection',
               'error':"",
               'titreH3':"Connectez vous, Please!!!"
    
    }
    template = loader.get_template('Security/sign-in.html')
    return HttpResponse(template.render(context, request))
    
def get_sign_up(request):
    context = {'title': 'Tkngo Sign-up',
    'titreH3':"Création du compte!!!"}
    template = loader.get_template('Security/sign-up.html')
    return HttpResponse(template.render(context, request))
#----------------------------------------------------------------------------------------------------------
#                 ERROR    400 500 404
#----------------------------------------------------------------------------------------------------------

def handler400(request,exception=None):
    return render(request,'erreurs/400.html',{},status=400)

def handler403(request,exception=None):
    return render(request,'erreurs/403.html',{},status=403)

def handler500(request,exception=None):
    return render(request,'erreurs/500.html',{},status=500)

def handler404(request,exception=None):
    return render(request,'erreurs/404.html',{},status=404)