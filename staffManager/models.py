from django.db import models
from ImageManager.models import AlbumInfo
from userManager.models import UserInfo

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
    
    
    #STAFF STATUS CONSTANTS
    STAFF_STATUS_DELETE = 0
    STAFF_STATUS_DEFAULT = 1
    
    STAFF_STATUS_CHOICES=(
        (STAFF_STATUS_DEFAULT,"default"),
        (STAFF_STATUS_DELETE,'delete'),
    )
    
     
    dealType = models.SmallIntegerField(choices=STAFF_DEAL_TYPE_CHOICES,default=STAFF_DEAL_TYPE_TRADE)
    albumInfo = models.ForeignKey(AlbumInfo)
    staffDesc = models.CharField(max_length=300)
    price = models.FloatField(default=0.0)
    position = models.CharField(max_length=100, default='-')
    longitute = models.FloatField(default=0.0)
    lagituite = models.FloatField(default=0.0)
    publisher = models.ForeignKey(UserInfo)  #The Publisher Info
    status = models.SmallIntegerField(choices = STAFF_STATUS_CHOICES, default=STAFF_STATUS_DEFAULT)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    