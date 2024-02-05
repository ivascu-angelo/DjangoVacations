# forms.py
from django import forms
from .models import Vacation

class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = '__all__'  # Assuming 'user' is included in your model fields

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(VacationForm, self).__init__(*args, **kwargs)
        if not (self.user and self.user.is_staff):
            # Assuming 'user' is the name of the field in your model you want to hide
            if 'user' in self.fields:
                self.fields.pop('user')
