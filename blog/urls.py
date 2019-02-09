# -*- coding:utf-8 -*-

from django.urls import re_path, path

from .views import PostCreateView, PostUpdateView, BlogPostListView,  \
    BlogSubscribeView, BlogListView

urlpatterns = [
    path('all/', BlogListView.as_view(), name='blogs_list'),
    re_path(r'(?P<blog_id>\d+)/subscribe', BlogSubscribeView.as_view(), name='blog_subscribe'),
    re_path(r'(?P<blog_id>\d+)/post/create', PostCreateView.as_view(), name='post_create'),
    re_path(r'(?P<blog_id>\d+)', BlogPostListView.as_view(), name='blog'),
]