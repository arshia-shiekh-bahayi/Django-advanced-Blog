from django.urls import path , include
from .views import *
from rest_framework.routers import *
router = DefaultRouter()
router.register('post',PostViewSet, basename='post')
app_name = 'api-v1'
urlpatterns = [
    # paths to function based views
    # path('post/<int:id>/', postDetail,name='post-detail'),
    # path('post/', postList,name='post-list'),
    # paths to class based views
    # path('post/', PostList.as_view(),name='post-list'),
    # path('post/<int:pk>/', PostDetail.as_view(),name='post-detail'),
    # paths to GenericViewSet views
    # path('post/', PostViewSet.as_view({'get':'list','post':'create'}), name='post-list'),
    # path('post/<int:pk>', PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name='post-detail')
]
urlpatterns += router.urls