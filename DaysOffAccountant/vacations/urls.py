from django.urls import path
from . import views
from .views import AddVacationView, VacationView

urlpatterns = [
  path("", VacationView.as_view(), name='vacations'),
  path('add/', AddVacationView.as_view(), name='add-vacation'),

]

