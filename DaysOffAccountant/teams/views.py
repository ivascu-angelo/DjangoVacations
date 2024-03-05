import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import CreateView, ListView, FormView
from DaysOffAccountant.teams.forms import InvitationForm
from DaysOffAccountant.teams.models import Team, InviteToTeam
from DaysOffAccountant.users.models import User


class AddTeamView(LoginRequiredMixin, CreateView):
    model = Team
    template_name = 'teams/create_team.html'
    success_url = reverse_lazy("teams")
    fields = ['name']

    def form_valid(self, form):
        team = form.save(commit=False)
        team.save()
        team.users.add(self.request.user)
        return super().form_valid(form)


class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'teams/teams.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return self.request.user.teams.all()


class InviteUserToTeamView(LoginRequiredMixin, FormView):
    template_name = 'teams/invite_to_team.html'
    form_class = InvitationForm
    success_url = reverse_lazy('invite')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['teams'] = self.request.user.teams.all()
        return kwargs

    def generate_unique_token(self):
        while True:
            token = secrets.token_urlsafe(20)
            if not InviteToTeam.objects.filter(token=token).exists():
                return token

    def form_valid(self, form):
        # cui trimit
        user_email = form.cleaned_data['user_email']
        team = form.cleaned_data['team']
        # de la cine trimit
        from_email = self.request.user.email
        token = self.generate_unique_token()
        invitation = InviteToTeam(email=user_email, token=token, team=team, was_accepted=False)
        invitation.save()
        accept_url = self.request.build_absolute_uri(reverse('accepted-invitation', args=[token]))
        email_body = f"Invitation to team:{team.name} LINK for acceptance:\n\n{accept_url}"
        send_mail(
            'Invitation to join a team',
            email_body,
            from_email,
            [user_email],
            fail_silently=False,
        )

        return super().form_valid(form)




class AcceptInvitationView(View):
    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        invitation = get_object_or_404(InviteToTeam, token=token)

        if invitation.was_accepted:
            message = 'This invitation has already been accepted.'
            context = {'team_name': None, 'message': message}
        else:
            user = User.objects.get(email=invitation.email)
            user.teams.add(invitation.team)
            invitation.was_accepted = True
            invitation.save()
            user.save()
            message = 'You have successfully joined the team!'
            context = {'team_name': invitation.team.name, 'message': message}

        return render(request, 'teams/accepted_invitation.html', context)
