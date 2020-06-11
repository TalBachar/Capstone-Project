from django.contrib import admin
from django.urls import path, include
from adoption  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.adoption, name = 'adoption'),
    path('accounts/', include('accounts.urls')),

]
