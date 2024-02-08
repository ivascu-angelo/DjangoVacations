from django.contrib import admin
from django.urls import path, include
from DaysOffAccountant.users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', users_views.SignupView.as_view(), name='signup'),
    path('login/', users_views.CustomLoginView.as_view(), name='login'),
    path('vacations/', include('DaysOffAccountant.vacations.urls')),
    path('admin/', admin.site.urls),
]