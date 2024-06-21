from django.contrib import admin
from django.urls import path

from ess import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/', views.home_view),
]
