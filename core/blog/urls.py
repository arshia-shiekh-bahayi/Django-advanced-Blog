from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from .views import *
app_name = 'blog'
urlpatterns = [
    # path('cbv-index', views.IndexView.as_view(),name='cbv-index'),
    # path('redirect/<int:pk>', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),
    path('post/', PostList.as_view(),name='post-list'),
    path('post/<int:pk>/' , PostDetailView.as_view(), name="post-detail")
    
]
