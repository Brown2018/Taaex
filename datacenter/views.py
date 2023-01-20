from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from datacenter.dao.dao_parametreSuplementaire import dao_parametreSuplementaire
from datacenter.dao.dao_valaurParams import dao_valaurParams

from profil.dao.dao_apps import dao_apps

# Create your views here.

def portal(request):
    context = {'titre': 'Portal',
                'apps':dao_apps.apps()}
    template = loader.get_template('TkngoPortal/index.html')
    return HttpResponse(template.render(context, request))

def paramettreProduit(request):
    try:
        listP=[]
        params=dao_parametreSuplementaire.getList()
        for i in params:
            listP.append(i.parametre)
        print("Params: ",listP)
        return JsonResponse(listP, safe=False)
    except Exception as e:
        return JsonResponse( "", safe=False)

def valeurParamettreProduit(request):
    try:
        listP=[]
        valeur=dao_valaurParams.getList()
        for i in valeur:
            listP.append(i.valeur)
        print("Valeur: ",listP)
        return JsonResponse(listP, safe=False)
    except Exception as e:
        return JsonResponse( "", safe=False)