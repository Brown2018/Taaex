from django.shortcuts import render, redirect

from datacenter.errors.printErrorFormat import printErrorFormat

def handler404(request, *args, **argv):
    response = render(request,'errors/error.html', {})
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    context={}
    response = render(request,'errors/error.html', context)
    response.status_code = 500
    return response