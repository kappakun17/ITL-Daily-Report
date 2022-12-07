from django.db import models
from user.models import User

# Create your models here.

class ITLGropuUserManager(models.Manager):
    def get_or_none(self, **kwargs):
       
       try:
           return self.get_queryset().get(**kwargs)
       except self.model.DoesNotExist:
           return None

class Company(models.Model):

    name = models.CharField(
        'name',
       max_length=200,
       help_text = ('外部講師の属する企業名を登録して下さい。'),
        blank=True,
        unique=True
        )
    class Meta:
        db_table = 'company'
        verbose_name = 'Company'
        verbose_name_plural = 'Company群'

    def __str__(self):
        return self.name

class Traineer(models.Model):
    traineer = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company, 
        on_delete=models.SET_DEFAULT, 
        default='no-company',
        related_name="user_traineer")
    
    def __str__(self):
        return '{}'.format(self.traineer)

    class Meta:
        db_table = 'user_traineer'
        verbose_name = 'トレーナー'
        verbose_name_plural = 'トレーナー群'



class ITLGroup(models.Model):
    group = models.PositiveSmallIntegerField('th',unique=True)

    def __str__(self):
        return str(self.group) + '期生'

    class Meta:
        db_table = 'ITL Group'
        verbose_name = 'ITLグループ'
        verbose_name_plural = 'ITLグループ群'

class ITLGroupUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_group')
    group = models.ForeignKey(ITLGroup, on_delete=models.PROTECT)

    objects = ITLGropuUserManager()


    def __str__(self):
        return str(self.user)


    class Meta:
        db_table = 'ITL Group User'
        verbose_name = 'ITLグループユーザー'
        verbose_name_plural = 'ITLグループユーザー群'



   

