from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
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
