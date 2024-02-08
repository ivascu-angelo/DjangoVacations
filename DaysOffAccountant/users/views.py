from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from DaysOffAccountant.users.forms import CustomUserCreationForm
from django.views import View


class SignupView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = '/vacations/'

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(UserPassesTestMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('vacations')

    def test_func(self):
        # comments by Angelo - blocheaza pe orice authenticat sa nu poate merge pe login
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        # daca esti authenticat si vrei sa mergi pe login iti iei red pe vacations
        return redirect('vacations')

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            auth_login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
