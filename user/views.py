#  -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

from blog.models import Post, BlogUser, MarkRead

# Create your views here.

class NewsView(View):
    '''
    /u/<user_name>/
    News for user.
    '''
    model = Post
    template_name = 'user/news.html'

    # def get(self, request, user_name):
    #     return render(request, self.template_name, {'user_name': user_name})
    def get(self, request):
        if not self.request.session.get('user_name'):
            return HttpResponseRedirect(reverse('login'))
        user = BlogUser.objects.get(username=self.request.session['user_name'])
        blogs = user.blogs.all()
        posts = Post.objects.filter(blog__in=blogs).order_by('ctime')
        # вытаскиваем отметки пачкой
        marks = {mark.post.id: True for mark in MarkRead.objects.filter(user=user, post__in=posts)}
        for post in posts:
            post.mark = marks.get(post.id, False)
        return render(request, self.template_name, {'post_list': posts})