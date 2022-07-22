from django.urls import path
from . import views

urlpatterns = [
    path('account-management/', views.AccountManagement.as_view())
    ]
