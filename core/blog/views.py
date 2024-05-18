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
def redirect_main(request):
     return HttpResponse("We are working on this page")
    #  return redirect('blog:api')

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context

""" def RedirectToMaktab(request):
     return redirect('http://maktabkhooneh.com')"""

class RedirectToMaktab(RedirectView):
    url = "http://maktabkhooneh.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):

    permission_required = 'blog.view_post'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 1
    ordering = '-created_date'

    # def get_queryset(self):
        # posts = Post.objects.filter(status = 1)
        # return posts

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    
"""class PostCreateView(FormView):

    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)"""

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post'
