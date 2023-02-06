from ResourceHumaines.models import Model_Postes_Fonction
import secrets
import string
class dao_poste(object):

    @staticmethod
    def toListPoste(entreprise,code_ent):
        try:
            return Model_Postes_Fonction.objects.filter(entreprise=entreprise,code_ent=code_ent)
        except Exception as ex:
            return None

    @staticmethod
    def toGetPoste(codex,entreprise):
        return Model_Postes_Fonction.objects.get(codex=codex,entreprise=entreprise)
   
    @staticmethod
    def toSave_or_exists( fonction,poste,entreprise,code):
      
        try:
            codex=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(100))

            valeur_=Model_Postes_Fonction(            
            fonction_id=fonction , 
            poste=poste,
            entreprise=entreprise,  
            codex=codex,code_ent=code)
            valeur_.save()
            return valeur_ 
           
        except Exception as ex:
            print('##### error',ex)
            return False

       