# models.py
from django.db import models

class ZUser(models.Model):
    zid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    inuse = models.BooleanField(default=True)
    remark = models.CharField(max_length=300, default=' ')
    zcme = models.IntegerField()
    zctm = models.DateTimeField(auto_now_add=True)
    zcby = models.CharField(max_length=100)
    zcat = models.CharField(max_length=300)
    zcre = models.CharField(max_length=100)
    zume = models.IntegerField()
    zutm = models.DateTimeField(auto_now_add=True)
    zuby = models.CharField(max_length=100)
    zuat = models.CharField(max_length=300)
    zure = models.CharField(max_length=100)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'zuser'