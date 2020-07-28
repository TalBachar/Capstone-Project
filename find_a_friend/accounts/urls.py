from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path ('signup', views.SignupClass.as_view(), name = 'signup'),
    path ('login', views.LoginClass.as_view(), name = 'login'),
    path ('logout', views.LogoutClass.as_view(), name = 'logout'),
	path('profile', views.Profile.as_view(), name='profile'),
	path('favorites', views.Favorites.as_view(), name='favorites')


]
