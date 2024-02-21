from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from DaysOffAccountant import settings
from DaysOffAccountant.users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', users_views.SignupView.as_view(), name='signup'),
    path('', include("django.contrib.auth.urls")),
    path('vacations/', include('DaysOffAccountant.vacations.urls')),
    path('admin/', admin.site.urls),
    path('teams/', include('DaysOffAccountant.teams.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)