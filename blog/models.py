# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Blog(models.Model):

    owner = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title


class Post(models.Model):

    blog = models.ForeignKey(Blog, db_index=True, on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    read = models.ManyToManyField(User, through='MarkRead',
                                  through_fields=['post', 'user'])

    def __str__(self):
        return self.title


class BlogUser(User):

    blogs = models.ManyToManyField(Blog, through='Subscriber',
                                  through_fields=['blog', 'user'])

    class Meta:
        abstract = True


class Subscriber(models.Model):

    blog = models.ForeignKey(Blog, db_index=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)


class MarkRead(models.Model):

    post = models.ForeignKey(Post, db_index=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True)
