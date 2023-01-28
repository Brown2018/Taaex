from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from datacenter.dao.dao_user_allow import *
 
from django.template import loader
from security.dao.dao_user import dao_user
import json
 

#si la personne n'est pas associée à la boutique on l'interdit de faire quoi que ce soit
def restruction_entre_shop_(view_func):

    def wrapper_func(request,*args,**kwargs):
        #-----------------  user ----------------------
        getuser_id=request.user.id                    #
        username= dao_user.getUtilisateur(getuser_id) #
        #----------------- / user ---------------------

        #pour recuperer l'id je doit d'abord transformer kwargs en json
        
        # je recupere l'id dans les paramettre de la fonction kwargs['id']
        id=kwargs['id']
        entreprise=daoShop.getShopById(id)

        if shop==0:
            context={
            'title': 'tkngo acces réfusé',
            'operation':"acces Interface",
            'error':"Vous etes pas autorisé à effectuer des operation dans cette instances"

            } 
            template = loader.get_template('TkngoShop/error/error.html')
            return HttpResponse(template.render(context,request)) 

        if dao_user_allow.get(username,shop.codeSecret):
            return view_func(request,*args,**kwargs)
        else:
            context={
            'title': 'tkngo acces réfusé',
            'operation':"acces Interface",
            'error':"Vous etes pas autorisé à effectuer des operation dans cette instances"

            } 
            template = loader.get_template('TkngoShop/error/error.html')
            return HttpResponse(template.render(context,request)) 
    return wrapper_func
            
