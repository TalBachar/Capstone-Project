
from django.contrib import admin
from django.urls import path
from MainPage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage, name= 'homePage')
]
