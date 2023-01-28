from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


class printErrorFormat(object):
    @staticmethod
    def printError(theClass,theMethod,theexection,request,page):
        try:
            print('toucher')
            message=""
            message="Il y a un problème au niveau de la class ",str(theClass)," sur la méthode (",str(theMethod),") qui dit ##",str(theexection)," la cause est ",str(theexection.__cause__)
            context = {'title': 'Erreur',
                        'message':message
                   
                    }
            template = loader.get_template(page)
            return HttpResponse(template.render(context, request))
        except Exception as e:
            context = {'title': 'title',
                       'message':e
            }
            template = loader.get_template(page)
            return HttpResponse(template.render(context, request))

