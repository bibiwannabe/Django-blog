from django.db import models
from tinymce.models import HTMLField

class Artical(models.Model):
    title = models.CharField(max_length=20)
    content = HTMLField()
    click = models.IntegerField()
    createdate = models.DateTimeField(auto_now=True)
    modifydate = models.DateTimeField(auto_now=True)
    uid = models.ForeignKey('user.UserInfo')
    def __str__(self):
        return self.title

class Comment(models.Model):
    uid = models.ForeignKey('user.UserInfo')
    aid = models.ForeignKey('user_articles.Artical')
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()


