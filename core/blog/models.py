from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  # this is a class to define posts for blog app
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  image = models.ImageField(null=True,blank=True)
  content = models.TextField()
  status = models.BooleanField()
  category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)

  created_date = models.DateTimeField(auto_add_now=True)
  updated_date = models.DateTimeField(auto_now=True)
  published_date = models.DateTimeField()
  
  def __str__(self):
    return self.title

class Category(models.Model):
  name = models.CharField(max_length=255)
  def __str__(self):
    return self.name
