from django.shortcuts import render
from .models import User


def users_list(request):
    users = User.objects.all()
    context = {'users': users, 'title': 'Список користувачів'}
    return render(request, "users/users_list.html", context)
