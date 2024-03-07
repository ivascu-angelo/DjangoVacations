from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from DaysOffAccountant.teams.models import Team
from DaysOffAccountant.users.models import User


class InvitationForm(forms.Form):
    user_email = forms.EmailField(label='User Email', required=True)
    team = forms.ModelChoiceField(queryset=Team.objects.none())

    def __init__(self, *args, **kwargs):
        teams = kwargs.pop('teams', Team.objects.none())
        super().__init__(*args, **kwargs)
        self.fields['team'].queryset = teams


    def clean_user_email(self):
        return self.cleaned_data.get('user_email')
