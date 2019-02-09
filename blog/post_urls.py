# -*- coding:utf-8 -*-

from django.urls import re_path, path

from blog.views import MarkPostView, PostView


urlpatterns = [
    re_path(r'(?P<pk>\d+)/mark', MarkPostView.as_view(), name='mark_post'),
    re_path(r'(?P<pk>\d+)/', PostView.as_view(), name='post'),
    # re_path(r'(?P<blog_id>\d+)/post/(?P<post_id>\d+)/update', PostUpdateView.as_view(), name='post_update'),
]