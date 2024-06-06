from rest_framework import serializers
from blog.models import *
"""A serializer class that can be used to serialize a category"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


"""A serializer class that can be used to serialize a post"""
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(
        source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    author_real = serializers.SerializerMethodField(method_name='author_real_name')
    class Meta:
        model = Post
        fields = ['id','author','author_real','image','title', 'content', 'snippet', 'category',
                  'status', 'relative_url', 'absolute_url', 'published_date']
        read_only_fields = ['author']
    
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def author_real_name(self,obj):
        prof  = Profile.objects.get(user__id=self.context.get('request').user.id)
        prof = str(prof.user.email)
        return prof
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)

        rep['category'] = CategorySerializer(instance.category,context= {'request':request}).data
        return rep
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)
        