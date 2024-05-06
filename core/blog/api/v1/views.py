from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post


data = {
    "id":1,
    "title":"post 1",
    "content":"post 1 content",
    "status":"published",
    "category":"category 1",
    "published_date":"2021-10-10"

}
@api_view()
def postList(request):
    return Response("ok")
@api_view()
def postDetail(request,id):
    return Response(data)