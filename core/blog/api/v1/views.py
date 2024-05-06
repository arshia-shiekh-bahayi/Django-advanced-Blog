from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import *

@api_view()
def postList(request):
    return Response("ok")
@api_view()
def postDetail(request,id):
    post =  Post.objects.get(pk=id)
    serializers = PosTSerializer(post)
    return Response(serializers.data)