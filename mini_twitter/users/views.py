from .models import User
from posts.models import Comment, Post
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список користувачів'
        return context


class UserDetailView(DetailView):
    model = User
    template_name = "users/user_detail.html"
    context_object_name = 'user_local'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Інформація про користувача'
        return context


class UserPostListView(ListView):
    template_name = "posts/post_list.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user__id=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['full_posts'] = get_full_posts(context['object_list'])
        context['title'] = f'Список постів користувача {get_object_or_404(User, pk=self.kwargs["pk"])}'
        return context


def get_full_posts(posts):
    full_posts = []
    for post in posts:
        full_posts.append((post, Comment.objects.filter(post__id=post.id).count()))
    return full_posts