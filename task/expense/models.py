from django.db import models

# Create your models here.
class creditform(models.Model):
    username = models.CharField(max_length=50)
    cfrom= models.CharField(max_length=50)
    camount= models.IntegerField()
    cdate= models.DateField()
    creason= models.CharField(max_length=100)
    cmode= models.CharField(max_length=20)

class debitform(models.Model):
    username = models.CharField(max_length=50)
    dfor= models.CharField(max_length=50)
    damount= models.IntegerField()
    ddate= models.DateField()
    dreason= models.CharField(max_length=20)
    dmode= models.CharField(max_length=20)
    ddet = models.CharField(max_length=100)