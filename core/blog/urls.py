from django.urls import path
from django.views.generic import *
from .views import *
app_name = 'blog'
urlpatterns = [
    # path('cbv-index', views.IndexView.as_view(),name='cbv-index'),
    # path('redirect/<int:pk>', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),
    path('post/', PostList.as_view(),name='post-list'),
    path('post/<int:pk>/' , PostDetailView.as_view(), name="post-detail"),
    path('post/create', PostCreateView.as_view(), name='post-create'),    
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]
