from django.db import models

# Create your models here.

class Article(models.Model):
    atitle = models.CharField(max_length=100)
    acontent = models.TextField(null=True)
    apub_datatime = models.DateTimeField(auto_now=True)
    aread = models.IntegerField()
    isDelete = models.BooleanField(default=True)