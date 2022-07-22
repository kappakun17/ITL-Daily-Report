from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('signin/', views.UserSignIn.as_view(), name='userSignIn'),
    path('signup/', views.UserSignUp.as_view(), name='userSIgnUp'),
    path('signup/confirm/', views.UserConfirm.as_view(), name='user-confirm'),
    path('signup/success/', views.UserSuccess.as_view(), name='user-success'),

    path('staff/signin', views.StaffSignIn.as_view(), name='staffSignIn'),
    path('staff/signup', views.StaffSignUp.as_view(), name='staffSignUp'),
    path('staff/signup/confirm', views.StaffConfirm.as_view(), name='staff-confirm'),
    path('staff/signup/success', views.StaffSuccess.as_view(), name='staff-success'),
    path('please-wait', views.pleaseWait.as_view(), name='please-wait'),
    path('signout/', views.SignoutView.as_view(), name='sign-out'),
    ]