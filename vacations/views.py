from django import forms
from django.shortcuts import render, redirect
from vacations.models import Vacation
from .forms import VacationForm


def vacation_overview(request):
    filtered_vacations = Vacation.objects.filter(user=request.user)
    return render(request, 'vacations/overview.html', {'vacations': filtered_vacations})


# class VacationForm(forms.ModelForm):
#     class Meta:
#         model = Vacation
#         fields = ['user', 'start_date', 'end_date']
#         widgets = {
#             'start_date': forms.DateInput(attrs={'type': 'date'}),
#             'end_date': forms.DateInput(attrs={'type': 'date'}),
#         }


def correct_vacation_dates(vacation):
    # Assuming vacation.start_date and vacation.end_date are datetime.date objects
    if vacation.end_date < vacation.start_date:
        # Swap the dates
        vacation.start_date, vacation.end_date = vacation.end_date, vacation.start_date
        vacation.save()  # Save the changes to the database


def add_vacation(request):
    if request.method == 'POST':
        form = VacationForm(request.POST, user=request.user)  # Pass the user here
        if form.is_valid():
            vacation = form.save(commit=False)
            if 'user' not in form.fields:
                vacation.user = request.user
            vacation.save()
            return redirect('vacations')
    else:
        form = VacationForm(user=request.user)  # Pass the user here as well

    return render(request, 'vacations/add_vacation.html', {'form': form})