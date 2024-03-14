from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from DaysOffAccountant.vacations.models import Vacation


class VacationView(LoginRequiredMixin, ListView):
    template_name = 'vacations/overview.html'
    context_object_name = 'vacations'
    success_url = reverse_lazy('vacations')

    def get_queryset(self):
        print('page load')
        return Vacation.objects.all()

    def get_context_data(self, **kwargs):
        return {"team_admin": self.request.user.is_team_admin, 'teams': self.request.user.teams.all(),
                **super().get_context_data(**kwargs)}

    def post(self, request, *args, **kwargs):
        is_team_admin = self.request.user.is_team_admin

        if is_team_admin:
            vacation_id = request.POST.get('vacation_id')
            vacation = get_object_or_404(Vacation, id=vacation_id)
            print(vacation.start_date, 'vacaiton')
            vacation.is_approved = True
            vacation.save()
            return HttpResponseRedirect(request.path)


class AddVacationView(LoginRequiredMixin, CreateView):
    model = Vacation
    template_name = 'vacations/add_vacation.html'
    success_url = reverse_lazy('vacations')
    fields = ['start_date', 'end_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.is_accepted = self.request.user.is_team_admin
        return super().form_valid(form)

