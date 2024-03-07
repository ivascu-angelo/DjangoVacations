from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views import View

from DaysOffAccountant.teams.models import InviteToTeam
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
        form.save_m2m()
        token = self.request.GET.get('invitation_token')
        invitation = InviteToTeam.objects.filter(email=user.email, was_accepted=False).first()

        if invitation and token == invitation.token:
            user.teams.add(invitation.team)
            invitation.was_accepted = True
            invitation.save()

        return redirect(self.success_url)


class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
