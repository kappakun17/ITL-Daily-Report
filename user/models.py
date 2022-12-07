from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.utils import timezone

# Create your models here.


class UserManager(BaseUserManager):
    # 各ユーザーのアカウント登録を処理
    def _create_user(self, first_name, last_name, email, password, **extra_fields):
        if not email:
            raise ValueError('Emailを入力してください')
        fixed_email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email = fixed_email, password=password,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    # ITL生徒が登録するとき
    def create_user(self,first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_traineer', False)
        return self._create_user(first_name, last_name, email, password)

    # スタッフが登録するとき
    def create_staff(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_traineer', False)
        return self._create_user(first_name, last_name, email, password)
    
    # 講師が登録するとき
    def create_traineer(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_traineer', True)
        return self._create_user(first_name, last_name, email, password)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        first_name = ''
        last_name = ''
        return self._create_user(first_name, last_name, email, password, **extra_fields)

    def get_or_none(self, **kwargs):
       
       try:
           return self.get_queryset().get(**kwargs)
       except self.model.DoesNotExist:
           return None

class User(AbstractBaseUser, PermissionsMixin):
    
    
    first_name = models.CharField(
        'first_name',
       max_length=150,
       help_text = ('あなたの名を英字で入力してください。'),
        blank=True
       )

    last_name = models.CharField(
        'last_name',
        max_length=150,
        help_text = ('あなたの姓を英字で入力してください。'),
         blank=True
        )

    email = models.EmailField(
        'email',
        max_length=250,
        unique=True,
        help_text=('社内のメールアドレスを入力してください。')
        )

    is_active = models.BooleanField(
        'is_active',
        default=True,
        help_text=('Falseにすると、アカウントとして認められません。')
        )

    is_activated = models.BooleanField(
        'is_activated',
        default=False,
        help_text=('アプリを利用するためにはTrueにしてください')
        )
    
    is_staff = models.BooleanField(
        'is_staff', 
        default=False,
        help_text=('ITLスタッフの場合はTrueにしてください。')
        )

    is_traineer = models.BooleanField(
        'is_traineer',
        default=False,
        help_text=('外部講師の場合はTrueにしてください。')
        )
    date_joined = models.DateTimeField('date time', default = timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELD = ['email']


    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'user_model'
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー群'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_email(subject, message, from_email, [self.email], **kwargs)

