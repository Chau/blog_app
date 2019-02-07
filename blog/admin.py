# -*- coding: utf-8 -*-
from django.contrib import admin

from blog.models import Blog, Post

# Register your models here.


admin.site.register(Blog)
admin.site.register(Post)