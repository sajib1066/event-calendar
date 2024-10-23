from django.contrib import admin
from django.urls import path, include

from .views import DashboardView


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("calendarapp.urls")),
    path("sport/", include("sport.urls", namespace="sport")),
]
