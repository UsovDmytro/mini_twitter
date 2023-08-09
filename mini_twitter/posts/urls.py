from django.urls import path
from .views import PostListView, CommentListView, UsersPostListView, add_post

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:user_id>/', UsersPostListView.as_view(), name='users_post_list'),
    path('posts/comments/', CommentListView.as_view(), name='comment_list'),
    path('add_post/', add_post, name='add_post'),
]