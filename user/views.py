#  -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic import View

from blog.models import Post, BlogUser

# Create your views here.

class NewsView(View):
    '''
    /u/<user_name>/
    News for user.
    '''

    template_name = 'user/news.html'

    def get(self, request, user_name):
        return render(request, self.template_name, {'user_name': user_name})


