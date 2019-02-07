# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

class BlogUser(User):

    blogs = models.ManyToManyField('Blog', through='Subscriber',
                                  through_fields=[ 'user', 'blog'])
    objects = UserManager()


class Blog(models.Model):

    owner = models.ForeignKey(BlogUser, db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)

    def subscribe(self, user_name):
        user = BlogUser.objects.get(username=user_name)
        user.blogs.add(self)

    def __str__(self):
        return self.title


class Post(models.Model):

    blog = models.ForeignKey(Blog, db_index=True, on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)
    title = models.CharField( max_length=200, verbose_name='Название поста')
    body = models.TextField(verbose_name='Сам пост')

    read = models.ManyToManyField(BlogUser, through='MarkRead',
                                  through_fields=['post', 'user'])

    def get_absolute_url(self):
        return '/blog/{blog_id}/post/{post_id}/'.format(blog_id=self.blog.id, post_id=self.pk)

    def __str__(self):
        return self.title


class Subscriber(models.Model):

    blog = models.ForeignKey(Blog, db_index=True, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, db_index=True, on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)


class MarkRead(models.Model):

    post = models.ForeignKey(Post, db_index=True, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, db_index=True, on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True)
