from GestionCouriers.models import Model_courrier,Model_TypeCourrier,Model_NatureCourrier,Model_AgentAffecterCourrier,Model_Annotation
import secrets
import string
class dao_courrier(object):

    @staticmethod
    def toListNature():
        try:
            return Model_NatureCourrier.objects.all()
        except Exception as ex:
            return None

    @staticmethod
    def toListypecourrier():
        try:
            return Model_TypeCourrier.objects.all()
        except Exception as ex:
            return None

    @staticmethod
    def toListCourrier(entreprise,code_ent):
        try:
            return Model_courrier.objects.filter(entreprise=entreprise,code_ent=code_ent,traiter=False,consulter=False,afecter=False,nature__nature="Entrant")
        except Exception as ex:
            return None

    @staticmethod
    def toListCourrierSortant(entreprise,code_ent):
        try:
            return Model_courrier.objects.filter(entreprise=entreprise,code_ent=code_ent,nature__nature="Sortant")
        except Exception as ex:
            return None
    @staticmethod
    def toListCourrierTraiter(entreprise,code_ent):
        try:
            c= Model_courrier.objects.filter(entreprise=entreprise,code_ent=code_ent,traiter=True)
            print(' ### ### ',c)
            return c

        except Exception as ex:
            return None
    @staticmethod
    def toListCourrierAffecter(entreprise,code_ent):
        try:
            c= Model_courrier.objects.filter(entreprise=entreprise,code_ent=code_ent,afecter=True)
            return c
        except Exception as ex:
            return None

    @staticmethod
    def toListCourrierAffecterMesAtaches(entreprise,code_ent,current_user_id):
        try:
            print('### ',entreprise,' ',code_ent,' ',current_user_id)
            a=Model_AgentAffecterCourrier.objects.filter(entreprise=entreprise,code_ent=code_ent,agent=current_user_id).select_related('agent','entreprise','courrier')
            print('### ',a)
            c=[]
            for item in a: 
                c.append(Model_courrier.objects.filter(entreprise=entreprise,code_ent=code_ent,traiter=False,afecter=True,pk=item.courrier_id).select_related('entreprise','typecourrir','nature','client_p','client_m'))
            return c
        except Exception as ex:
            print('## ',ex)
            return None

    @staticmethod
    def toListeCourrierTraiteMestache(entreprise,code_ent,current_user_id):
        try:
            a=Model_AgentAffecterCourrier.objects.filter(entreprise=entreprise,code_ent=code_ent,agent=current_user_id).select_related('agent','entreprise','courrier')
            c=[]
            for item in a: 
                c.append(Model_courrier.objects.filter(entreprise=entreprise,code_ent=code_ent,traiter=True,afecter=True,pk=item.courrier_id).select_related('entreprise','typecourrir','nature','client_p','client_m'))
            return c
        except Exception as ex:
            print('## ',ex)
            return None


    @staticmethod
    def toGetCourrier(codex,entreprise):
        return Model_courrier.objects.get(codex=codex,entreprise=entreprise)
    
    @staticmethod
    def toSave_or_exists( libele ,concerne,reference,typecourrir, 
            nature, 
            code_ent, 
            entreprise, 
            utilisateur, 
            client_m, 
            client_p,client_intitule,decision,anotation,client_p_exp,client_m_exp,client_intitule_exp):         
        try:
            codex=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(100))
            valeur_=Model_courrier(            
            libele=libele ,   
            concerne=concerne, 
            reference=reference, 
            typecourrir_id=typecourrir, 
            nature_id=nature, 
            code_ent=code_ent, 
            entreprise=entreprise, 
            utilisateur=utilisateur, 
            client_m_id=client_m, 
            client_p_id=client_p,
            codex=codex,
            client_intitule=client_intitule,
            decision=decision,
            client_p_exp_id=client_p_exp,
            client_m_exp_id=client_m_exp,
            client_intitule_exp=client_intitule_exp
            )
            valeur_.save()
            return valeur_ 
        except Exception as ex:
            print('##### error',ex)
            return False

    @staticmethod
    def toAffecterAgent( courrier,agent,entreprise,code):
      
        try:
            codex=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(100))
            cour=Model_courrier.objects.get(pk=courrier)
            cour.afecter=True
            cour.save()
            valeur_=Model_AgentAffecterCourrier(            
            courrier_id=courrier , 
            agent_id=agent,
            entreprise=entreprise,  
            codex=codex,code_ent=code)
            valeur_.save()
            return valeur_ 
           
        except Exception as ex:
            print('##### error',ex)
            return False

    @staticmethod
    def toListCourrierAffecte(entreprise,code_ent,id):
        try:
            return Model_AgentAffecterCourrier.objects.filter(entreprise=entreprise,code_ent=code_ent,courrier__id=id)
        except Exception as ex:
            print(' #### ',ex)
            return None
    @staticmethod
    def toAnnotation( courrier_codex,code,entreprise,annotation,agent):
        try:
            codex=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(100))
            courrier=Model_courrier.objects.get(codex=courrier_codex)
            valeur_=Model_Annotation(            
            courrier_id=courrier.id , 
            code_ent=code,
            entreprise=entreprise, 
            annotation=annotation,
            employer_id=agent.id,
            codex=codex)
            valeur_.save()
            return valeur_ 
           
        except Exception as ex:
            print('##### error',ex)
            return False

    @staticmethod
    def toAnnotationCloture( courrier_codex,code,entreprise,annotation,agent):
        try:
            codex=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(100))
            courrier=Model_courrier.objects.get(codex=courrier_codex)
            courrier.traiter=True
            courrier.save()
            valeur_=Model_Annotation(            
            courrier_id=courrier.id , 
            code_ent=code,
            entreprise=entreprise, 
            annotation=annotation,
            employer_id=agent.id,
            codex=codex)
            valeur_.save()
            return valeur_ 
           
        except Exception as ex:
            print('##### error',ex)
            return False