from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=200)#投稿者
    images = models.ImageField(upload_to='')#画像のアップロード場所
    good = models.IntegerField()#いいね数
    read = models.IntegerField()#既読数
    readtext = models.CharField(max_length=200)#既読した人の名前
