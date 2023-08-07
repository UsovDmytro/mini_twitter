from django.urls import path
from .views import PostListView, CommentListView, UsersPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:user_id>/', UsersPostListView.as_view(), name='users_post_list'),
    path('comments/', CommentListView.as_view(), name='comment_list'),
]