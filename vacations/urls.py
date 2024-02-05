from django.urls import path
from . import views

urlpatterns = [
  path("", views.vacation_overview, name='vacations'),
  path('add/', views.add_vacation, name='add-vacation'),

]

