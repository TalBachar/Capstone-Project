from django.urls import path
from .views import *

app_name = 'search'

urlpatterns = [
    path('pet', SearchView.as_view(), name='pet'),
]
