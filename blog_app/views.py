# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.urls import reverse


class LoginView(View):
    '''
    /login/
    Login without password
    '''

    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_name = request.POST.get('user_name')
        request.session['user_name'] = user_name
        return HttpResponseRedirect(reverse('news'))


class LogoutView(View):
    '''
    /logout/
    Clean session
    '''

    def get(self, request):
        request.session.flush()
        return HttpResponseRedirect(reverse('login'))


class MainView(View):
    '''
    url: /
    View for main page
    '''

    def get(self, request):

        if request.session.get('user_name'):
            return HttpResponseRedirect(reverse('news'))
        else:
            return HttpResponseRedirect(reverse('login'))


