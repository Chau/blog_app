# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

class BlogUser(User):

    blogs = models.ManyToManyField('Blog', through='Subscriber',
                                  through_fields=[ 'user', 'blog'])
    objects = UserManager()


class Blog(models.Model):

    # owner = models.ForeignKey(BlogUser, db_index=True, on_delete=models.CASCADE)
    owner = models.OneToOneField(BlogUser, db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)

    def subscribe(self, user_name):
        user = BlogUser.objects.get(username=user_name)
        Subscriber.objects.create(user=user, blog=self)

    def unsubscribe(self, user_name):
        user = BlogUser.objects.get(username=user_name)
        Subscriber.objects.filter(user=user, blog=self).delete()
    #     clean user read marks for all post in this blog
        MarkRead.objects.filter(user=user, post__in=self.post_set.all()).delete()

    def is_subscriber(self, user_name):
        '''
        Return True if @user_name is subscribed to blog
        :param user_name: String
        :return: Boolean
        '''
        if not user_name:
            return False
        user = BlogUser.objects.get(username=user_name)
        return Subscriber.objects.filter(blog=self, user=user).exists()

    def get_subscribers(self):
        return [subs.user for subs in Subscriber.objects.filter(blog=self)]

    def __str__(self):
        return self.title


class Post(models.Model):

    blog = models.ForeignKey(Blog, db_index=True, on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)
    title = models.CharField( max_length=200, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')

    read = models.ManyToManyField(BlogUser, through='MarkRead',
                                  through_fields=['post', 'user'])

    def mark(self, username, checked):
        '''
        Mark post as read or unmark
        :param username: String
        :param checked: Boolean. Read or unread
        :return:
        '''
        user = BlogUser.objects.get(username=username)
        if checked:
            MarkRead.objects.get_or_create(user=user, post=self)
        else:
            MarkRead.objects.filter(user=user, post=self).delete()

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
