# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):

    owner = models.ForeignKey(User, db_index=True)
    title = models.CharField(max_length=100, db_index=True)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)


class Post(models.Model):

    blog = models.ForeignKey(Blog, db_index=True)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)
    title = models.CharField(max_length=200)
    body = models.TextField()


class Subscriber(models.Model):

    blog = models.ForeignKey(Blog, db_index=True)
    user = models.ForeignKey(User, db_index=True)
    ctime = models.DateTimeField(auto_now_add=True, db_index=True)


class MarkRead(models.Model):

    post = models.ForeignKey(Post, db_index=True)
    user = models.ForeignKey(User, db_index=True)
    ctime = models.DateTimeField(auto_now_add=True)
