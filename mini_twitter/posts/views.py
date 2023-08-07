from django.shortcuts import render
from .models import Post, Comment
from django.db.models import Count

def posts_list(request):
    posts = Post.objects.all()
    full_posts = []
    for post in posts:
        full_posts.append((post, Comment.objects.filter(post__id=post.id).aggregate(Count("id"))['id__count']))

    context = {'full_posts': full_posts, 'title': 'Список постів'}
    return render(request, "posts/posts_list.html", context)


def comments_list(request):
    posts = Comment.objects.all().values('post').distinct()
    comments_post = []
    for post in posts:
        print(Post.objects.get(id=post['post']))
        comments_post.append((Post.objects.get(id=post['post']), Comment.objects.filter(post__id=post['post'])))

    context = {'comments_post': comments_post, 'title': 'Список коментів'}
    return render(request, "posts/comments_list.html", context)
