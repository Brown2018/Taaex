from datacenter.models import Model_valeurParametreeSuplementaireProduit
from datacenter.errors.printErrorFormat import *
class dao_valaurParams(object):
    @staticmethod
    def getList():
        return Model_valeurParametreeSuplementaireProduit.objects.all() 

    @staticmethod
    def toSave_or_exists(valeur):
        try:
            try:
                val=Model_valeurParametreeSuplementaireProduit.objects.get(valeur=valeur)
                return val.id
            except Exception as ex:
                valeur_=Model_valeurParametreeSuplementaireProduit()
                valeur_.valeur=valeur
                valeur_.save()
                return valeur_.id
        except  Exception as e:
            printErrorFormat.printError("dao_valaurParams","toSave_or_exists",e)
            return None
