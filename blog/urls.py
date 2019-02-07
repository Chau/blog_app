# -*- coding:utf-8 -*-

from django.urls import re_path

from .views import post_create

urlpatterns = [
    re_path('(?P<blog_id>\d+)/post/create',  post_create)
]