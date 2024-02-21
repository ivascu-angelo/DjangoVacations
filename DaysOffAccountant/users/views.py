import logging

from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView
from django.views import View

from DaysOffAccountant.users.models import User


class SignupView(CreateView):
    model = User
    template_name = 'users/signup.html'
    success_url = '/login/'
    fields = ['email', 'password']


class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

    # def form_valid(self, form):
    #     email = form.cleaned_data.get('email')
    #     password = form.cleaned_data.get('password')
    #     user = authenticate(self.request, email=email, password=password)

