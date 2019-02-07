# -*- coding:utf-8 -*-

from django import forms

from .models import Post


class PostForm(forms.ModelForm):

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
