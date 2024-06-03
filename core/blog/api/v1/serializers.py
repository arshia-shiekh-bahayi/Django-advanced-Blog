from rest_framework import serializers
from blog.models import *
"""A serializer class that can be used to serialize a post"""
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    category = serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['id','author','title','content','snippet','category','status','relative_url','absolute_url','published_date']
    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    def to_representation(self, instance):
        return super().to_representation(instance)
"""A serializer class that can be used to serialize a category"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'