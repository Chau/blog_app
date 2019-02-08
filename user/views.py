#  -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post, BlogUser

# Create your views here.

class NewsView(ListView):
    '''
    /u/<user_name>/
    News for user.
    '''
    model = Post
    template_name = 'user/news.html'

    # def get(self, request, user_name):
    #     return render(request, self.template_name, {'user_name': user_name})

    def get_queryset(self):
        user = BlogUser.objects.get(username=self.request.session['user_name'])
        blogs = user.blogs.all()
        return Post.objects.filter(blog__in=blogs).order_by('ctime')
