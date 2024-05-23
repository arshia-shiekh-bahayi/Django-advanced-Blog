from django.urls import path , include
from .views import *
app_name = 'api-v1'
urlpatterns = [
    # path('post/<int:id>/', postDetail,name='post-detail'),
    # path('post/', postList,name='post-list'),
    path('post/', PostList.as_view(),name='post-list'),
    path('post/<int:pk>/', PostDetail.as_view(),name='post-detail'),
]
