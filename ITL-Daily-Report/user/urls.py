from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('sign-in', views.userSignIn, name='userSignIn'),
    path('sign-up', views.userSignUp, name='userSIgnUp'),
    path('staff/sign-in', views.staffSignIn, name='staffSignIn'),
    path('staff/sign-up', views.staffSignUp, name='staffSignUp')]