from django import forms
from django.core.exceptions import ValidationError

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
        user_email = self.cleaned_data.get('user_email')
        # dai clean la input
        if not User.objects.filter(email=user_email).exists():
            # dai error daca userul nu exista
            raise ValidationError("This email does not belong to a registered user.")
        return user_email

