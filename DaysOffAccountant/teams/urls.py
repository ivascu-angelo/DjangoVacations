from django.urls import path

from DaysOffAccountant.teams.views import AddTeamView, TeamListView, InviteUserToTeamView, AcceptInvitationView
from DaysOffAccountant.vacations.views import VacationView

urlpatterns = [
    path("", TeamListView.as_view(), name='teams'),
    path('invite/accept/<str:token>/', AcceptInvitationView.as_view(), name='accepted-invitation'),
    path('invite/', InviteUserToTeamView.as_view(), name='invite'),
    path('add', AddTeamView.as_view(), name='create_team'),
    path('<str:team_name>/', VacationView.as_view(), name='vacation-by-team'),
]