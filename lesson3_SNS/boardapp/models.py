from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=200)#投稿者
    images = models.ImageField(upload_to='')#画像のアップロード場所
    good = models.IntegerField(null=True,blank=True,default=0)#いいね数
    read = models.IntegerField(null=True,blank=True,default=0)#既読数
    readtext = models.CharField(max_length=200,null=True,blank=True,default='root')#既読した人の名前
