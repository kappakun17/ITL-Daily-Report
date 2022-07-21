from django.urls import path
from . import views

urlpatterns = [
    path('user/dialy/', views.UserDialy.as_view()),
    path('user/dialy/detail/<int:detail_id>', views.UserDialyDetail.as_view()),
    path('user/dialy/edit/<int:edit_id>', views.UserDialyEdit.as_view()),
    path('user/dialy/post/message', views.UserDialyPostMessage.as_view())
    ]
