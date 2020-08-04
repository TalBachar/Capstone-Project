from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import (ProfileView,)


app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile_update', views.profile_update, name='profile_update'),
	path('profile/', views.ProfileHome.as_view(), name='profile'),
	path('user/<str:username>/', ProfileView.as_view(), name='myprofile'),


]
