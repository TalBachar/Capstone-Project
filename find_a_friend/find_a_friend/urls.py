from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from pets  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.adoption, name = 'pets'),
    path('accounts/', include('accounts.urls')),

]
