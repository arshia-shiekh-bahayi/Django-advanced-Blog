from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import *
from .models import Post , Category
from .forms import *
# Create your views here.

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
    
class PostList(ListView):

    model = Post
    # queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 1
    ordering = '-created_date'
    # def get_queryset(self):
        # posts = Post.objects.filter(status = 1)
        # return posts

class PostDetailView(DetailView):
    model = Post
    
"""class PostCreateView(FormView):

    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)"""

class PostCreateView(CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post'