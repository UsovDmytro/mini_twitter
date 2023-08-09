from django.urls import path
from .views import UserListView, UserDetailView, UserPostListView


urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/posts', UserPostListView.as_view(), name='user_post_list'),
]