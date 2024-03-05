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

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super(SignupView, self).form_valid(form)


class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
