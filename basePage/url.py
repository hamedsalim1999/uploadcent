from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'core'
urlpatterns = [
path('',views.HomeTemplateView.as_view(),name='index'),
path('<str:uid>',views.ArticleTemplateView.as_view(),name='article'),



    
]

