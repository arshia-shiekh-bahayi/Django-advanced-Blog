from django import forms
from .models import Post
"""A class that inherits from model post (in models.py) and have the same field (except some) to create a object post"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'category', 'published_date']