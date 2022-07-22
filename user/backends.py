from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        print('通りました')
        try:
            user = User.objects.get(email=email)
        except User.DoseNotExist:
            print('ありませんでした。')
            return None
        else:
            if user.check_password(password):
                return user