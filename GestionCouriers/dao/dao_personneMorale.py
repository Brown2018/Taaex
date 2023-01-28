from GestionCouriers.models import Model_PersonneMorale
import secrets
import string
class dao_personneMorale(object):

    @staticmethod
    def toListPersonneMorale(entreprise,code_ent):
        try:
            return Model_PersonneMorale.objects.filter(entreprise=entreprise,code_ent=code_ent)
        except Exception as ex:
            return None

    @staticmethod
    def toGetPersonneMorale(codex,entreprise):
        return Model_PersonneMorale.objects.get(codex=codex,entreprise=entreprise)
   
    @staticmethod
    def toSave_or_exists( intitule ,   
            rccm, 
            siren, 
            Effectifs, 
            Date_creation_entreprise, 
            code_ent, 
            entreprise, 
            Forme_juridique,
            utilisateur, 
            specialisation, 
            adresse,apropos,email,tel):
      
        try:
            codex=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(100))

            valeur_=Model_PersonneMorale(            
            intitule=intitule ,   
            rccm=rccm, 
            siren=siren, 
            Effectifs=Effectifs, 
            Date_creation_entreprise=Date_creation_entreprise, 
            code_ent=code_ent, 
            Forme_juridique=Forme_juridique,
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

       