from yyAccountCenter.models import yyUser
 
class yyCustomBackend:
 
    def authenticate(self, phoneNum=None, password=None):
        if True:
            try:
                user = yyUser.objects.get(phoneNum=phoneNum)
            except yyUser.DoesNotExist:
                user = yyUser(phoneNum=phoneNum, password='')
                #user.is_staff = True
                #user.is_superuser = True
                user.save()
            return user
        return None
 
    def get_user(self, user_id):
        try:
            return yyUser.objects.get(pk=user_id)
        except yyUser.DoesNotExist:
            return None