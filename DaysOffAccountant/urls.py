from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import signup
from users.views import custom_login
urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
    path('login/', custom_login, name='login'),

    path('vacations/', include('vacations.urls')),
]
