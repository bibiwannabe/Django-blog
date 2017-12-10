from django.db import models
import pymysql


class Articles(models.Model):

    title = models.CharField(max_length=32,default='title')
    cont = models.TextField(null=True)

    def __str__(self):

        return self.title


