from django.conf import settings
 
import os

from django.core.files.storage import default_storage

class dao_deletefile(object):
    #Génerateur de chemin
    @staticmethod
    def pathdeleter(path):
        try:
            if default_storage.exists(path):
                default_storage.delete(path)
                print('######### path exists')                       
            # on li la feuil
            return 1
        except Exception as e:
            print('Erreur Delete file')
            print(e)
            return 0