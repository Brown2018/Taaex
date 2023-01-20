from datacenter.models import Model_parametreSuplementaireProduit
from datacenter.errors.printErrorFormat import *

class dao_parametreSuplementaire(object):
    @staticmethod
    def getList():
        return Model_parametreSuplementaireProduit.objects.all() 

    @staticmethod
    def toSave_or_exists(params):
        try:
            try:
                val=Model_parametreSuplementaireProduit.objects.get(parametre=params)
                return val.id
            except Exception as ex:
                param=Model_parametreSuplementaireProduit()
                param.parametre=params
                param.save()
                return param.id
        except  Exception as e:
            printErrorFormat.printError("dao_parametreSuplementaire","toSave_or_exists",e)
            return None
