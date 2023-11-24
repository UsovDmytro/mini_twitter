from django.urls import path
from .views import RegisterView, login_view, logout_view
from .views import UserListView, UserDetailView, UserPostListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/posts', UserPostListView.as_view(), name='user_post_list'),
]
