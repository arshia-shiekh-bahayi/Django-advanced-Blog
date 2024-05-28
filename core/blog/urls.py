from django.urls import path , include
from django.views.generic import *
from .views import *
app_name = 'blog'
urlpatterns = [
    # Main url
    path('', redirect_main, name='redirect'),
    # Urls to class based view in views.py
    path('post/', PostListView.as_view(),name='post-list'),
    path('post/<int:pk>/' , PostDetailView.as_view(), name="post-detail"),
    path('post/create', PostCreateView.as_view(), name='post-create'),    
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # a path to include paths in api/v1/urls.py 
    path('api/v1/', include('blog.api.v1.urls'),name='api-v1'),
]
