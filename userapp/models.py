# models.py
from django.db import models

class ZUser(models.Model):
    zid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    inuse = models.BooleanField(default=True)
    remark = models.CharField(max_length=300, default=' ')
    zcme = models.IntegerField(null=True)
    zctm = models.DateTimeField(auto_now_add=True)
    zcby = models.CharField(max_length=100, null=True)
    zcat = models.CharField(max_length=300, null=True)
    zcre = models.CharField(max_length=100, null=True)
    zume = models.IntegerField(null=True)
    zutm = models.DateTimeField(auto_now_add=True)
    zuby = models.CharField(max_length=100, null=True)
    zuat = models.CharField(max_length=300, null=True)
    zure = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'zuser'