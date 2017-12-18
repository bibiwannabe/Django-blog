#coding=utf-8
from django.db import models
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    userpassword = models.CharField(max_length=40)
    useremail = models.CharField(max_length=30)
    userphone = models.CharField(max_length=11)
# Create your models here.
