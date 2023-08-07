from django.urls import path
from .views import posts_list, comments_list, user_posts

urlpatterns = [
    path('', posts_list, name='posts'),
    path('<int:user_id>/', user_posts, name='user_posts'),
    path('comments/', comments_list, name='comments'),
]