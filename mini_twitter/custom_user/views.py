from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from custom_user.forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django.contrib.auth import login, logout

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') # URL, на який перенаправляє користувача після успішної реєстрації
    template_name = 'registration.html' # Шаблон, який ви використовуєте для своєї сторінки реєстрації

def login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'login.html', {'form':form})




def logout_view(request):
    logout(request)
    return redirect('login')
