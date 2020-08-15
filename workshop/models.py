from django.db import models

# Create your models here.

class Arttherapy(models.Model) :

    heading = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    readm = models.URLField(max_length=200 , blank=True , null=True)

class Publication(models.Model) :

    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False, blank = True ,null = True )
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    contiR = models.URLField(max_length=200 , blank=True , null=True)    

class updates(models.Model) :
    month = models.CharField(max_length=100)
    U_date = models.IntegerField()
    U_heading = models.TextField()
    U_desc = models.TextField()
    link = models.URLField(max_length=200 , blank=True , null=True)
   
class Gallery(models.Model) :

    G_img =  models.ImageField(upload_to='pics')
    G_heading = models.CharField(max_length=100)
    G_desc = models.TextField()