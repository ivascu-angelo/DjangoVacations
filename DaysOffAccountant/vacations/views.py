from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from DaysOffAccountant.vacations.models import Vacation
from .forms import VacationForm


class VacationListView(LoginRequiredMixin, ListView):
    model = Vacation
    template_name = 'vacations/overview.html'

    def get_queryset(self):
        return Vacation.objects.filter(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacations'] = self.get_queryset()
        return context


class AddVacationView(LoginRequiredMixin, CreateView):
    model = Vacation
    form_class = VacationForm
    template_name = 'vacations/add_vacation.html'
    success_url = reverse_lazy('vacations')

    def form_valid(self, form):
        vacation = form.save(commit=False)
        vacation.user = self.request.user

        if vacation.end_date < vacation.start_date:
            vacation.start_date, vacation.end_date = vacation.end_date, vacation.start_date

        vacation.save()
        return redirect(self.success_url)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
