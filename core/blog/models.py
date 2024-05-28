from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import *
# Create your models here.

"""A model using in blog app. contains different parts and works like a twit """
class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    def __str__(self):
        return self.title

"""A model that just have a name. It is used with a many-to-many relationship to category part in post model"""
class Category(models.Model):
  name = models.CharField(max_length=255)
  def __str__(self):
    return self.name
