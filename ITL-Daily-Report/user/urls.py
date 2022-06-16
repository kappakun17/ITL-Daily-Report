from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('sign-in', views.userSignIn, name='userSignIn'),
    path('staff/sign-in', views.staffSignIn, name='staffSignIn')]