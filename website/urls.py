from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('online-kennzahlen', views.kennzahlen, name="online_kennzahlen"),
    path('dashboard-software-kostenlos', views.dashboard_kostenlos, name="dashboard_kostenlos"),
]
