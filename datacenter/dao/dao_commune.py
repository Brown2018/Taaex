
from datacenter.models import Model_Commune


class dao_commune(object):

   
    @staticmethod
    def toListComune():
        return Model_Commune.objects.all()
    
   