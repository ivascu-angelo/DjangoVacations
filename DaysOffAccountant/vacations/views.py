from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from DaysOffAccountant.teams.models import Team
from DaysOffAccountant.users.models import User
from DaysOffAccountant.vacations.models import Vacation


class VacationView(LoginRequiredMixin, ListView):
    model = Vacation
    template_name = 'vacations/overview.html'
    context_object_name = 'vacations'
    success_url = reverse_lazy('vacations')

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        team_id = self.request.GET.get('team')
        if team_id:
            team = get_object_or_404(Team, id=team_id)
            users_in_team = User.objects.filter(teams=team)
            queryset = queryset.filter(user__in=users_in_team)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_teams = self.request.user.teams.all()
        context['teams'] = Team.objects.filter(pk__in=user_teams)
        return context


class AddVacationView(LoginRequiredMixin, CreateView):
    model = Vacation
    template_name = 'vacations/add_vacation.html'
    success_url = reverse_lazy('vacations')
    fields = ['start_date', 'end_date']

    def form_valid(self, form):
        vacation = form.save(commit=False)
        vacation.user = self.request.user

        if vacation.end_date < vacation.start_date:
            vacation.start_date, vacation.end_date = vacation.end_date, vacation.start_date

        vacation.save()
        return redirect(self.success_url)

