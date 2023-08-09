from .models import Post, Comment
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['full_posts'] = get_full_posts(context['object_list'])
        context['title'] = 'Список постів'
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post__id=self.kwargs["pk"])
        context['title'] = 'Інформація про пост'
        return context


def get_full_posts(posts):
    full_posts = []
    for post in posts:
        full_posts.append((post, Comment.objects.filter(post__id=post.id).count()))
    return full_posts


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    # def get_success_url(self):
    #     return reverse_lazy("post_list")


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])

        return context
