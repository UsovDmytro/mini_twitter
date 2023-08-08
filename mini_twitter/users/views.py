from .models import User
from django.views.generic import ListView


class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список постів користувачів'
        return context

