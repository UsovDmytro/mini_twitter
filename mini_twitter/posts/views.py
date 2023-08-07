from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.db.models import Count
from users.models import User

def posts_list(request):
    posts = Post.objects.all()
    full_posts = get_full_posts(posts)
    title = 'Список постів'
    context = {'full_posts': full_posts, 'title': title}
    return render(request, "posts/posts_list.html", context)


def user_posts(request, user_id):
    posts = Post.objects.filter(user__id=user_id)
    full_posts = get_full_posts(posts)
    title = f'Список постів користувача {get_object_or_404(User, pk=user_id)}'
    context = {'full_posts': full_posts, 'title': title}
    return render(request, "posts/posts_list.html", context)


def comments_list(request):
    posts = Comment.objects.all().values('post').distinct()
    comments_post = []
    for post in posts:
        comments_post.append((Post.objects.get(id=post['post']), Comment.objects.filter(post__id=post['post'])))

    context = {'comments_post': comments_post, 'title': 'Список коментів'}
    return render(request, "posts/comments_list.html", context)


def get_full_posts(posts):
    full_posts = []
    for post in posts:
        full_posts.append((post, Comment.objects.filter(post__id=post.id).aggregate(Count("id"))['id__count']))
    return full_posts
