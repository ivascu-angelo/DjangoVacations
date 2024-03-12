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

    def get_initial(self):
        initial = super().get_initial()
        invitation_token = self.request.GET.get('invitation_token')
        if invitation_token:
            invitation = InviteToTeam.objects.filter(token=invitation_token).first()
            if invitation and not invitation.was_accepted:
                initial['email'] = invitation.email
        return initial

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        invitation_token = self.request.GET.get('invitation_token')
        if invitation_token:
            invitation = InviteToTeam.objects.filter(token=invitation_token).first()
            if not invitation.was_accepted:
                user.teams.add(invitation.team)
        return redirect(self.success_url)

class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
