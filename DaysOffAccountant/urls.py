from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from DaysOffAccountant import settings
from DaysOffAccountant.users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', users_views.SignupView.as_view(), name='signup'),
    path('login/', users_views.CustomLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('vacations/', include('DaysOffAccountant.vacations.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)