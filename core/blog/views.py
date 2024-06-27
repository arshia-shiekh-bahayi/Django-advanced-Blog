from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.mixins import *
from rest_framework.decorators import *
from rest_framework.response import Response
# Create your views here.
"""A function based view to redirect users to post-list with ('post/) url """
def redirect_main(request):
    return redirect('accounts/api/v1/registration/')

"""A class based view inheriting from Django Generic Views (ListView) to show a list of objects of model post """    
class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = 'blog.view_post'
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'
    paginate_by = 1
    ordering = '-created_date'

"""A class based view inheriting from Django Generic Views (DetailVIew) to show details of an object of a models by Pk"""
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

"""A class based view inheriting from Django Generic Views (CreateView) to show a form for creating a object of a model and creating it"""
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

"""A class based view inheriting from Django Generic Views (UpdateView) to show a filled form for updating a model"""    
class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

"""A class based view inheriting from Django Generic Views (DeleteView) to delete a object of a model"""
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post'
