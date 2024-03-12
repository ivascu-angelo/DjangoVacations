import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
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
    support_email = "support@vacation-manager.com"

    def get_form_kwargs(self):
        kwargs = super(InviteUserToTeamView, self).get_form_kwargs()
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
        support_email = 'support@vacation-manger.com'
        if User.objects.filter(email=user_email, teams=team).exists():
            form.add_error('user_email', 'This user is already a member of the team.')
            return self.form_invalid(form)

        token = self.generate_unique_token()
        InviteToTeam.objects.create(email=user_email, token=token, team=team, was_accepted=False)

        accept_url = self.request.build_absolute_uri(reverse('accepted-invitation', args=[token]))
        email_body = f"Invitation to team:{team.name} LINK for acceptance:\n\n{accept_url}"
        send_mail(
            'Invitation to join a team',
            email_body,
            support_email,
            [user_email],
            fail_silently=False,
        )

        return super().form_valid(form)


class AcceptInvitationView(View):

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        # ia din DB instanta in baza tokenului
        invitation = get_object_or_404(InviteToTeam, token=token, was_accepted=False)
        user = User.objects.filter(email=invitation.email).first()

        if not user:
            return redirect(f'/signup?invitation_token={token}')
        else:
            user.teams.add(invitation.team)
            invitation.was_accepted = True
            message = 'You have successfully joined the team!'
            context = {'team_name': invitation.team.name, 'message': message}

        return render(request, 'teams/accepted_invitation.html', context)


