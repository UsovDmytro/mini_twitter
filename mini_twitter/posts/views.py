from django.shortcuts import get_object_or_404
from .models import Post, Comment
from users.models import User
from django.views.generic import ListView


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['full_posts'] = get_full_posts(context['object_list'])
        context['title'] = 'Список постів'
        return context


class UsersPostListView(ListView):
    template_name = "posts/post_list.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user__id=self.kwargs['user_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['full_posts'] = get_full_posts(context['object_list'])
        context['title'] = f'Список постів користувача {get_object_or_404(User, pk=self.kwargs["user_id"])}'
        return context


class CommentListView(ListView):
    model = Comment
    template_name = "posts/comment_list.html"
    context_object_name = 'comments'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = Comment.objects.all().values_list('post', flat=True).distinct()
        comments_post = []
        for post in posts:
            comments_post.append((Post.objects.get(id=post), Comment.objects.filter(post__id=post)))

        context['comments_post'] = comments_post
        context['title'] = 'Список коментів'
        return context


def get_full_posts(posts):
    full_posts = []
    for post in posts:
        full_posts.append((post, Comment.objects.filter(post__id=post.id).count()))
    return full_posts
