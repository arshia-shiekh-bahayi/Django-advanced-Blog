from rest_framework import serializers
from blog.models import Post
"""A serializer class that can be used to serialize a post"""
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','author','title','content','category','status','published_date']