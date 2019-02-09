# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, View, DeleteView

from .models import Post, Blog
from .forms import PostForm

# Create your views here.


class PostCreateView(CreateView):

    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_initial(self):
        return {'blog': self.kwargs.get('blog_id')}

    def get_context_data(self, **kwargs):
        # добавляем в контекст объект Blog
        self.blog = get_object_or_404(Blog, pk=self.kwargs['blog_id'])
        kwargs['blog'] = self.blog
        context = super(PostCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        post = form.save()
        # TODO: send_email

        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']


class PostView(DetailView):
    model = Post


class MarkPostView(View):

    def get(self, request, pk):
        checked = request.GET.get("checked")
        print(checked)
        username = request.session.get('user_name')
        if not username:
            return JsonResponse({'status': 'error', 'message': 'error2'})

        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'error3'})
        post.mark(username, checked=='true')
        return JsonResponse({'status': 'ok'})

#     def post(self, request):
#         post_id = request.POST.get('post_id')
#         # TODO: if not post_id
#         checked = request.POST.get("checked")
#         print(checked)
#         username = request.session.get('user_name')
# #         TODO: if not username
#         try:
#             post = Post.objects.get(id=post_id)
#         except Post.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'error'})
#         post.mark(username, checked)
#         return JsonResponse({'status': 'ok'})


class BlogPostListView(ListView):

    model = Post

    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        # добавляем в контекст объект Blog
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        context['is_subscriber'] = self.blog.is_subscriber(self.request.session.get('user_name', ''))
        return context

    def get_queryset(self):
        self.blog = get_object_or_404(Blog, pk=self.kwargs['blog_id'])
        return Post.objects.filter(blog=self.blog)


class BlogListView(ListView):

    model = Blog
    template_name = 'blog/all.html'

    def get_queryset(self):
        return Blog.objects.all().order_by('-ctime')


class BlogSubscribeView(View):

    def post(self, request, blog_id):
        blog = get_object_or_404(Blog, pk=blog_id)
        user_name = request.session.get('user_name')
        if not user_name:
            # TODO: редирект на логин
            pass
        if request.POST.get('subscribe'):  # checkbox
            blog.subscribe(user_name)
        else:
            blog.unsubscribe(user_name)
        # возвращаемся в блог
        return HttpResponseRedirect(reverse('blog', kwargs={'blog_id': blog.id}))

