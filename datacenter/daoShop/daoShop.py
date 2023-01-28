from gestionStockVente.models import Model_shop
from gestionStockVente.models import Model_Usser_Allow

from django.conf import settings
from random import randint
 

class daoShop(object):

    @staticmethod
    def addShop(user,categorie,designation,banier_link,description,commune,quartier,avenu,vu):
        try:
            secrete=randint(0, 999)
            secrete=str(secrete)+designation
            addshop=Model_shop.objects.update_or_create(user=user,categorie_id=categorie,designation=designation,banier_link=banier_link,description=description,commune_id=commune,quartier=quartier,avenu=avenu,vu=vu,codeSecret=secrete)
            Model_Usser_Allow.objects.update_or_create(user=user,codeSecret=secrete)

            return addshop[0]
        except Exception as ex:
            print('###### cause error',str(ex.__cause__))
            return ex

    
    @staticmethod
    def addbanier(id,link):
        try:
 
            banier=Model_shop.objects.get(pk=id)
            if settings.DEBUG:
                banier.banier_link="/media/"+link
            else:
                 banier.banier_link=link
            banier.save()
            return banier
        except Exception as e:
            print('ERROR ',e)
            return e 
     
    @staticmethod
    def getShopById(id):
        try:
            banier=Model_shop.objects.get(pk=id)
            return banier
        except Model_shop.DoesNotExist as e:
            print('##### ex shop ',e)
            return 0
    @staticmethod
    def getShopByUserAndId(user,id):
        try:
            shop=Model_shop.objects.get(pk=id,user__utilisateur__username=user)
            return shop
        except Exception as e:
             return e

    @staticmethod
    def listShopsByUser(user):
        try:
            shop=Model_shop.objects.filter(user__utilisateur__username=user)
            return shop
        except Exception as e:
             return e

    @staticmethod
    def listShops():
        try:
            shop=Model_shop.objects.all()
            return shop
        except Exception as e:
             return e

    @staticmethod
    def getShopByCode(code):
        print('Touché code',code)
        try:
            banier=Model_shop.objects.get(codeSecret=code)
            return banier
        except Model_shop.DoesNotExist as e:
            print('##### ex getShopByCode ',e)
            return 0
            
    @staticmethod
    def listShopsByCategories(type_):
        try:
            shop=Model_shop.objects.filter(categorie=type_)
            return shop
        except Exception as e:
             return e
