from django.urls import path
from . import views


urlpatterns = [
    path('user/dialy/detail', veiw.userDialyDetail.as_view())
    ]
