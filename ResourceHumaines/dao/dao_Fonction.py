from ResourceHumaines.models import Model_Employer_Fonction
import secrets
import string
class dao_Fonction(object):

    @staticmethod
    def toListFonction(entreprise,code_ent):
        try:
            return Model_Employer_Fonction.objects.filter(entreprise=entreprise,code_ent=code_ent)
        except Exception as ex:
            return None

    @staticmethod
    def toGetFonction(codex,entreprise):
        return Model_Employer_Fonction.objects.get(codex=codex,entreprise=entreprise)
   
    @staticmethod
    def toSave_or_exists( fonction,entreprise,code):
      
        try:
            codex=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(100))

            valeur_=Model_Employer_Fonction(            
            fonction=fonction , 
            entreprise=entreprise,  
            codex=codex,code_ent=code)
            valeur_.save()
            return valeur_ 
           
        except Exception as ex:
            print('##### error',ex)
            return False

       