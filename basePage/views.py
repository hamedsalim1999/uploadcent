from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from . import models
# Create your views here.
class Home(TemplateView):
    template_name = 'post.html'
    page_name = 'index'
    model = models.Post
    context_object_name = 'post_show'
class HomeTemplateView(ListView):
    template_name = 'post.html'
    page_name = 'home'
    model = models.Post
    context_object_name = 'post_show'
class ArticleTemplateView(DetailView):
    template_name = 'post.html'
    page_name = 'post'
    pk_url_kwarg = 'uid'
    model = models.Post
    context_object_name = 'article_detail'
