# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Blog, Post, BlogUser
from .forms import PostAdminForm

# Register your models here.

class BlogUserAdmin(admin.ModelAdmin):

    fields = ['username', 'email']


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Blog)
admin.site.register(Post, PostAdmin)
admin.site.register(BlogUser, BlogUserAdmin)