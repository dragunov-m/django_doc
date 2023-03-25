from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
User = get_user_model()


def home(request):
    return render(request, 'auth_task/homepage.html')


def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('auth_task:home')
    else:
        messages.error(request, 'Invalid login or password')
    return render(request, 'auth_task/login_page.html')


def logout_page(request):
    logout(request)
    return redirect('auth_task:home')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_task:home')
    else:
        form = UserCreationForm()
    return render(request, 'auth_task/registration_page.html', {'form': form})
