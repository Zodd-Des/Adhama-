from django.db import models

# Create your models here.

class Job(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

class Testimony(models.Model):

    name = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

class Blogs(models.Model):

    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    descr = models.TextField()

    
class LatestPosts(models.Model):

    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    descr = models.TextField()

class Training(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

   



