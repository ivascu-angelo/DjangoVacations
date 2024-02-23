from django.urls import path

from DaysOffAccountant.teams.views import AddTeamView, TeamListView
from DaysOffAccountant.vacations.views import VacationView

urlpatterns = [
    path("", TeamListView.as_view(), name='teams'),
    path('add', AddTeamView.as_view(), name='create_team'),
    path('<str:team_name>/', VacationView.as_view(), name='vacation-by-team'),  # Vacanțe filtrate după echipă
]

