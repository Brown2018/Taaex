"""Tkngo_ URL Configuration

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
from django.contrib import admin
from django.urls import path,re_path
from . import views
#from django.conf.urls import url

urlpatterns = [
    path('', views.get_sign_in,name="security_sign_in"),
    # Sign - up
    path('sign-up', views.get_sign_up,name="security_sign_up"),
    path('postSignup', views.creer_un_user,name="creer_un_user"),
    # / sign - up
    path('login', views.signIn,name="login_view"),
    # out 
    path('login', views.logout_view,name="logout_view"),
    # resent mail
    path('resentMessage', views.resentMessage,name="security_resentMessage"),
    # activation user count
    re_path(r'^activationUser/$', views.activationUser, name='activationUser'),
    #verification user name
    re_path(r'^verificationUserName/form/$', views.get_Username, name='security_verificationUserName'),
    #verification mail
    re_path(r'^verificationUserEmail/form/$', views.get_Useremail, name='security_verificationUserEmail'),
    
   
]
