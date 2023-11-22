from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('posts/<int:pk>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
]