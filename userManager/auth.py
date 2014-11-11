from userManager.models import UserInfo
class yyCustomBackend:
    def authenticate(self, phoneNum=None, password=None):
        try:
            user = UserInfo.objects.get(phoneNum=phoneNum)
        except UserInfo.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user
        return None