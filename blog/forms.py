# -*- coding:utf-8 -*-

from threading import Thread

from django import forms
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

from .models import Post


def send_emails_to_subscribers(post):
    messages = []
    subj = "Привет! У нас новый пост!"
    email_text = 'Заходите к нам на огонек!'

    for email in [user.email for user in post.blog.get_subscribers()]:
        messages.append((subj, email_text, settings.DEFAULT_FROM_EMAIL, [email,]))

    thread = Thread(target=send_mass_mail, kwargs={'datatuple': messages})
    thread.start()


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('blog', 'title', 'body')

    def save(self, commit=True):
        post = super(PostAdminForm, self).save(commit=commit)
        send_emails_to_subscribers(post)
        return post


class PostForm(PostAdminForm):

    # title = forms.CharField(label='Заголовок')
    # body = forms.CharField(widget=forms.Textarea, label='Text')
    # blog = forms.CharField(widget=forms.HiddenInput())
    #
    class Meta:
        model = Post
        fields = ('blog', 'title', 'body')
        widgets = {'blog': forms.HiddenInput()}


    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['blog'].widget = forms.HiddenInput()
