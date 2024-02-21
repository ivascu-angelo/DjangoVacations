from django.urls import path

from DaysOffAccountant.teams.views import AddTeamView, TeamListView

urlpatterns = [
  path("", TeamListView.as_view(), name='teams'),
  path('add', AddTeamView.as_view(), name='create_team'),

]
