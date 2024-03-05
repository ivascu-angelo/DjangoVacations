from django.db import models
from django.utils.crypto import get_random_string


class Team(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class InviteToTeam(models.Model):
    def __str__(self):
        return self.token

    email = models.EmailField(max_length=100)
    was_accepted = models.BooleanField(default=False)
    token = models.CharField(max_length=20, unique=True, default=get_random_string)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='invitations')
