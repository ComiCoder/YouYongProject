from django.db import models
from ImageManager.models import AlbumInfo
from userManager.models import UserInfo
from YouYongProject import specSetting

# Create your models here.
class StaffInfo(models.Model):
    
    #STAFF_DEAL_TYPE CONSTANTS
    STAFF_DEAL_TYPE_TRADE = 1   #Trade
    STAFF_DEAL_TYPE_PRESENT = 2 #Present
    STAFF_DEAL_TYPE_SWITCH = 3  #Switch
    
    STAFF_DEAL_TYPE_CHOICES = (
                    (STAFF_DEAL_TYPE_TRADE,"Trade"),
                    (STAFF_DEAL_TYPE_PRESENT,"Present"),
                    (STAFF_DEAL_TYPE_SWITCH,"Switch"),
                    )
    
    
     
    dealType = models.SmallIntegerField(choices=STAFF_DEAL_TYPE_CHOICES,default=STAFF_DEAL_TYPE_TRADE)
    albumInfo = models.ForeignKey(AlbumInfo,null=True)
    staffDesc = models.CharField(max_length=300, null=True)
    price = models.FloatField(default=0.0)
    position = models.CharField(max_length=100, default='-')
    longitute = models.FloatField(default=0.0, null=True)
    lagituite = models.FloatField(default=0.0, null=True)
    publisher = models.ForeignKey(UserInfo, null=True)  #The Publisher Info
    status = models.SmallIntegerField(choices = specSetting.INFO_STATUS_CHOICES, default=specSetting.INFO_STATUS_DEFAULT)
    createTime = models.DateTimeField(auto_now_add=True, null=True)
    updateTime = models.DateTimeField(auto_now=True, null=True)
    
