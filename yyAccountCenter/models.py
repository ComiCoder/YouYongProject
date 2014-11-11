from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class YYUserManager(BaseUserManager):
    def create_user(self,phoneNum, password=None):
        if not phoneNum:
            raise ValueError('User must have a phoneNum')
        
        user = self.model(
               phoneNum=phoneNum,
            )
        
        user.set_password(password)
        user.save(self._db)
        return user
    
    def create_superuser(self, phoneNum, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(phoneNum,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

        

class YYUser(AbstractBaseUser):
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
    
    REG_TYPE_PHONE = 1
    REG_TYPE_WEIBO = 2
    REG_TYPE_WEIXIN = 3
    
    ICON_UPLOAD_PATH = "images/profile_icon/"
    
    
    phoneNum = models.CharField(max_length=20, unique=True)
    nickName = models.CharField(max_length=30, null=True)
    smallIconURL = models.ImageField(upload_to=ICON_UPLOAD_PATH, null=True)
    largeIconURL = models.ImageField(upload_to=ICON_UPLOAD_PATH, null=True)
    gender = models.SmallIntegerField(choices = GENDER_CHOICES, default=GENDER_NULL)
    selfDesc = models.CharField(max_length=300,null=True)
    address = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    type = models.SmallIntegerField(choices=USER_TYPE_CHOICES,default=USER_TYPE_NORMAL)
    regProvince = models.SmallIntegerField(null=True)
    regCity=models.SmallIntegerField(null=True)
    authValue = models.SmallIntegerField(default=0)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    
    
    objects = YYUserManager()
    
    USERNAME_FIELD = 'phoneNum'
    REQUIRED_FIELDS = []
    
    def get_full_name(self):
        return self.phoneNum + self.nickName
    
    def get_short_name(self):
        return self.phoneNum
    
    def __unicode__(self):
        return self.phoneNum
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
        