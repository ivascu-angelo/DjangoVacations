from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from DaysOffAccountant.users.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.views import View


class SignupView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = '/vacations/'

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('vacations')

    def handle_no_permission(self):
        # daca esti auth, atunci mergi pe vacations
        return redirect(self.get_success_url())

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            auth_login(self.request, user, backend='DaysOffAccountant.users.backends.EmailBackend')
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
