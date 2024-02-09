from django import forms
from django_flatpickr.widgets import DatePickerInput

from DaysOffAccountant.vacations.models import Vacation


class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = ['start_date', 'end_date']
        widgets = {
            "start_date": DatePickerInput(),
            "end_date":DatePickerInput,
        }

    def __init__(self, *args, **kwargs):
        #scoate user din fields ca sa nu apara in form.
        #Modelform incearca sa iti genereze form cu toate fields din model
        self.user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)
