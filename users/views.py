from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from users.forms import CustomUserCreationForm


def authentication(request):
    return HttpResponse('Auth page for now')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object that the form returns
            username = user.get_username()  # Assuming your user model has a username field
            password = form.cleaned_data.get('password1')  # Get the raw password
            user = authenticate(request, username=username, password=password)  # Authenticate the user
            if user is not None:
                auth_login(request, user)  # Log the user in
                return redirect('vacations')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('vacations')  # Redirect to a named URL pattern
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    auth_logout(request)
    return redirect('login')
