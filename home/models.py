from django.db import models

# Create your models here.



class ElasticDemo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
class Url(models.Model):
    url = models.CharField(max_length=100)
    label = models.CharField(max_length=100,default=False)