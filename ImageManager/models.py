from django.db import models

# Create your models here.
class ImageInfo(models.Model):
    
    IMG_UPLOAD_PATH = "images/normalImgs/"
    
    IMAGE_TYPE_STAFF = 1
    IMAGE_TYPE_ACTIVITY = 2
    
    IMAGE_TYPE_CHOICES = (
      (IMAGE_TYPE_STAFF,"Staff"),
      (IMAGE_TYPE_ACTIVITY,"Activity"),
    )
    
    imgURL = models.ImageField(upload_to=IMG_UPLOAD_PATH)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    type = models.SmallIntegerField(choices=IMAGE_TYPE_CHOICES,default=IMAGE_TYPE_STAFF)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    
    
class AlbumInfo(models.Model):
    
    ALBUM_STATUS_DELETE = 0
    ALBUM_STATUS_DEFAULT = 1
    
    
    ALBUM_STATUS_CHOICES=(
        (ALBUM_STATUS_DEFAULT,"default"),
        (ALBUM_STATUS_DELETE,'delete'),
    )
    
    
    title = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=300,default='')
    status=models.SmallIntegerField(choices=ALBUM_STATUS_CHOICES,default=ALBUM_STATUS_DEFAULT)
    
    images = models.ManyToManyField(ImageInfo, through='Album2Image')
    
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    
    
class Album2Image(models.Model):
    ALBUM2IMG_STATUS_DELETE = 0
    ALBUM2IMG_STATUS_DEFAULT = 1
    
    
    ALBUM2IMG_STATUS_CHOICES=(
        (ALBUM2IMG_STATUS_DEFAULT,"default"),
        (ALBUM2IMG_STATUS_DELETE,'delete'),
    )
    
    albumInfo = models.ForeignKey(AlbumInfo)
    ImageInfo = models.ForeignKey(ImageInfo)
    isPrimary = models.BooleanField(default="False")
    status=models.SmallIntegerField(choices=ALBUM2IMG_STATUS_CHOICES,default=ALBUM2IMG_STATUS_DEFAULT)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    
    
    
    
    