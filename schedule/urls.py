from django.urls import path
from . import views


urlpatterns = [
    path('user/schedule', views.UserSchedule.as_view()),
    path('user/schedule/get/list', views.GetEvents.as_view()),
    ]
