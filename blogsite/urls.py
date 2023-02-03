
from django.contrib import admin
from django.urls import path
from blogsite.views import all_blogs, blog_post

urlpatterns = [
    path('', all_blogs, name='all_blogs'),
    path('blog/<slug>', blog_post, name='blog_post'),

]