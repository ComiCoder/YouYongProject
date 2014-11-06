from rest_framework import serializers
from userManager.models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('phoneNum','nickName','smallIconURL','largeIconURL',
                  'gender','selfDesc','address','zipcode','email',
                  'type','regProvince','regCity',
                  'authValue','createTime','updateTime')