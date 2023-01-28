from GestionCouriers.models import Model_PersonnePhysique
import secrets
import string
class dao_personnePysique(object):

    @staticmethod
    def toListPersonnePhysique(entreprise,code_ent):
        try:
            return Model_PersonnePhysique.objects.filter(entreprise=entreprise,code_ent=code_ent)
        except Exception as ex:
            return None

       

    @staticmethod
    def toGetPersonnePhysique(codex,entreprise):
        return Model_PersonnePhysique.objects.get(codex=codex,entreprise=entreprise)
    

   
    @staticmethod
    def toSave_or_exists( nom ,   
            postnom, 
            prenom, 
            sexe, 
            age, 
            code_ent, 
            entreprise, 
            utilisateur, 
            specialisation, 
            adresse,apropos,email,tel):
      
        try:
            codex=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(100))
            valeur_=Model_PersonnePhysique(            
            nom=nom ,   
            postnom=postnom, 
            prenom=prenom, 
            sexe=sexe, 
            age=age, 
            code_ent=code_ent, 
            entreprise=entreprise, 
            utilisateur=utilisateur, 
            specialisation=specialisation, 
            adresse=adresse,
            codex=codex,
            apropos=apropos,
            email=email,
            telephone=tel)
            valeur_.save()
            return valeur_ 
           
        except Exception as ex:
            print('##### error',ex)
            return False

       