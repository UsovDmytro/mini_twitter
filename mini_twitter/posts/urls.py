from django.urls import path
from .views import posts_list, comments_list

urlpatterns = [
    path('', posts_list, name='posts'),
    path('comments/', comments_list, name='comments'),
]