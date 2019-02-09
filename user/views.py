#  -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post, BlogUser, MarkRead

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
        posts = Post.objects.filter(blog__in=blogs).order_by('ctime')
        # вытаскиваем отметки пачкой
        marks = {mark.post.id: True for mark in MarkRead.objects.filter(user=user, post__in=posts)}
        for post in posts:
            post.mark = marks.get(post.id, False)
        return posts
