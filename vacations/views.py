from django import forms
from django.shortcuts import render, redirect
from vacations.models import Vacation
from .forms import VacationForm


def vacation_overview(request):
    filtered_vacations = Vacation.objects.filter(user=request.user)
    return render(request, 'vacations/overview.html', {'vacations': filtered_vacations})


def correct_vacation_dates(vacation):
    if vacation.end_date < vacation.start_date:
        vacation.start_date, vacation.end_date = vacation.end_date, vacation.start_date
        vacation.save()


def add_vacation(request):
    if request.method == 'POST':
        form = VacationForm(request.POST, user=request.user)
        if form.is_valid():
            vacation = form.save(commit=False)
            if 'user' not in form.fields:
                vacation.user = request.user
            vacation.save()
            return redirect('vacations')
    else:
        form = VacationForm(user=request.user)

    return render(request, 'vacations/add_vacation.html', {'form': form})