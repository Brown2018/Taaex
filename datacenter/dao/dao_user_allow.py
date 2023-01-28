from datacenter.models import Model_Usser_Allow

class dao_user_allow(object):

    @staticmethod
    def save_update(user,secrete):
        try:
            Model_Usser_Allow.objects.update_or_create(user=user,codeSecret=secrete)
        except Exception as e:
            return e

    @staticmethod
    def get(user,secrete):
        try:
            Model_Usser_Allow.objects.get(user=user,codeSecret=secrete)
            return True

        except Model_Usser_Allow.DoesNotExist as e:
            return False


    @staticmethod
    def listcode(user):
        try:
            return Model_Usser_Allow.objects.filter(user__utilisateur__username=user)
        except Exception as e:
            return e