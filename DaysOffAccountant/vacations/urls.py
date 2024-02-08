from django.urls import path
from . import views
from .views import AddVacationView, VacationListView

urlpatterns = [
  path("", VacationListView.as_view(), name='vacations'),
  path('add/', AddVacationView.as_view(), name='add-vacation'),

]

