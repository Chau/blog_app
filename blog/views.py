# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.


def post_create(request):
    return HttpResponse('hello')


class BlogView(ListView):

    
