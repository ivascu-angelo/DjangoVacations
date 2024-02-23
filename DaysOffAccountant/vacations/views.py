from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from DaysOffAccountant.teams.models import Team
from DaysOffAccountant.users.models import User
from DaysOffAccountant.vacations.models import Vacation


class VacationView(LoginRequiredMixin, ListView):
    template_name = 'vacations/overview.html'
    context_object_name = 'vacations'
    success_url = reverse_lazy('vacations')

    def get_queryset(self):
        return Vacation.objects.filter(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        return {"teams": self.request.user.teams.all(), **super().get_context_data(**kwargs)}


class AddVacationView(LoginRequiredMixin, CreateView):
    model = Vacation
    template_name = 'vacations/add_vacation.html'
    success_url = reverse_lazy('vacations')
    fields = ['start_date', 'end_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



