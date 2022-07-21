from django.urls import path
from . import views


app_name = 'profile'

urlpatterns = [
    path('initial-profile/user', views.UserInitialProfile.as_view()),
    path('initial-profile/staff', views.StaffInitialProfile.as_view()),
    path('dashboard/user/profile', views.ProfileView.as_view()),
    ]