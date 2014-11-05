from django.db import models

# Create your models here.

#UserInfo 
class UserInfo(models.Model):
    
    #GENDER Constants
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_NULL = 3
    GENDER_CHOICES = (
        (GENDER_MALE,'Male'),
        (GENDER_FEMALE,'Female'),
        (GENDER_NULL,'-')              
    )
    
    #UserType Constants
    USER_TYPE_NORMAL = 1
    USER_TYPE_ADMIN = 2
    
    USER_TYPE_CHOICES = (
        (USER_TYPE_NORMAL,'Normal'),
        (USER_TYPE_ADMIN,'Admin')
    )
    
    
    phoneNum = models.CharField(max_length=20, null=True)
    nickName = models.CharField(max_length=30, null=True)
    smallIconURL = models.URLField(max_length=100, null=True)
    largeIconURL = models.URLField(max_length=100, null=True)
    gender = models.SmallIntegerField(choices = GENDER_CHOICES, default=GENDER_NULL)
    selfDesc = models.CharField(max_length=300,null=True)
    address = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    type = models.SmallIntegerField(choices=USER_TYPE_CHOICES,default=USER_TYPE_NORMAL)
    regProvince = models.SmallIntegerField(null=True)
    regCity=models.SmallIntegerField(null=True)
    authValue = models.SmallIntegerField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
  
    
    
        