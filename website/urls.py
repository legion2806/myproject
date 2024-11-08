from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('weather/', views.weather, name='weather'),
    path('camps/', views.camps, name='camps'),
    path('info/', views.info, name='info'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='website/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]