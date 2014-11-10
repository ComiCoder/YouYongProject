from django.db import models
from userManager.models import UserInfo
from staffManager.models import StaffInfo
from YouYongProject import specSetting

# Create your models here.
class PostInfo(models.Model):
    postUser = models.ForeignKey(UserInfo)
    postStaff = models.ForeignKey(StaffInfo)
    description = models.CharField(max_length=specSetting.GLOBAL_DESC_MAX_LENGTH)
    status = models.SmallIntegerField(choices = specSetting.INFO_STATUS_CHOICES, default=specSetting.INFO_STATUS_DEFAULT)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    