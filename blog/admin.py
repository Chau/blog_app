# -*- coding: utf-8 -*-
from django.contrib import admin

from blog.models import Blog, Post, BlogUser

# Register your models here.

class BlogUserAdmin(admin.ModelAdmin):

    fields = ['username']

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(BlogUser, BlogUserAdmin)