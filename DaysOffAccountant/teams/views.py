from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.db.models import Count
from DaysOffAccountant.teams.models import Team


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
        user_teams = self.request.user.teams.all()
        return user_teams
