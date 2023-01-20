from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse

import os

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator

from django.http import Http404


#################################################
#------------ Time ------------------------
#import datetime
from datetime import datetime, date, timedelta, time
# Create your views here.
# Create your views here.
@login_required(login_url='login_view')
def dashboard(request):
    print('touchE')
    try:
        context = {'title': 'Dashboard'}
        template = loader.get_template('dashboard.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {'login': 'login',
                   'erreur':e
        }
        template = loader.get_template('Security/login.html')
        return HttpResponse(template.render(context, request))

@login_required(login_url='login_view')
def profil(request):
    try:
        context = {'title': 'Profil'}
        template = loader.get_template('profil.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {'login': 'login',
                   'erreur':e
        }
        template = loader.get_template('Security/login.html')
        return HttpResponse(template.render(context, request))

@login_required(login_url='login_view')
def personneMorale(request):
    try:
        context = {'title': 'Personne Morale'}
        template = loader.get_template('personneMorale.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {'login': 'login',
                   'erreur':e
        }
        template = loader.get_template('Security/login.html')
        return HttpResponse(template.render(context, request))

@login_required(login_url='login_view')
def personnePhysique(request):
    try:
        context = {'title':'Personne Physique'}
        template = loader.get_template('personnePhysique.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {'login' : 'login',
                   'erreur':e
        }
        template = loader.get_template('Security/login.html')
        return HttpResponse(template.render(context, request))

@login_required(login_url='login_view')
def courrierEntrant(request):
    try:
        context = {'title':'Courriers entrants'}
        template = loader.get_template('courrierEntrant.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {'login' : 'login',
                   'erreur':e
        }
        template = loader.get_template('Security/login.html')
        return HttpResponse(template.render(context, request))

@login_required(login_url='login_view')
def courrierSortant(request):
    try:
        context = {'title':'Courriers entrants'}
        template = loader.get_template('courrierSortant.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {'login' : 'login',
                   'erreur':e
        }
        template = loader.get_template('Security/login.html')
        return HttpResponse(template.render(context, request))


@login_required(login_url='login_view')
def listeCourrier(request):
    try:
        context = {'title':'Courriers entrants'}
        template = loader.get_template('listeCourrier.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {'login' : 'login',
                   'erreur':e
        }
        template = loader.get_template('Security/login.html')
        return HttpResponse(template.render(context, request))