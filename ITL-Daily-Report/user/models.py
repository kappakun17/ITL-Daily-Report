from django.db import models
from django.utils import timezone

# Create your models here.


class UserManager(models.Manager):
   def get_or_none(self, **kwargs):
       
       try:
           return self.get_queryset().get(**kwargs)
       except self.model.DoesNotExist:
           return None

class User(models.Model):
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)
    email = models.EmailField('email',max_length=250)
    password = models.CharField('password', max_length=50)
    is_active = models.BooleanField('is_active', default=False)
    date_joined = models.DateTimeField('date time', default = timezone.now)

    manager = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'user_model'
        verbose_name = 'ITLユーザー'
        verbose_name_plural = 'ITLユーザー群'



class Staff(models.Model):
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)
    email = models.EmailField('email',max_length=250)
    password = models.CharField('password', max_length=50)
    is_staff = models.BooleanField('is_staff', default = True)
    is_active = models.BooleanField('is_active', default=False)
    is_traineer = models.BooleanField('is_traineer', default=False)
    date_joined = models.DateTimeField('date time', default = timezone.now)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'staff_model'
        verbose_name = 'ITLスタッフ'
        verbose_name_plural = 'ITLスタッフ群'