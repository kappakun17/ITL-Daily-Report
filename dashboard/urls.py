from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserDashboard.as_view(), name='dashboard-user'),
    path('staff/', views.StaffDashboard.as_view(), name='dashboard-staff'),
    ]
