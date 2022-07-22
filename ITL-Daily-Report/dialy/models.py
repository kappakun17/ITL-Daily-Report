from django.db import models
from user.models import User
from schedule.models import Schedule
from django.utils import timezone

# Create your models here.

class DialyManager(models.Manager):
    def get_or_none(self, **kwargs):
       
       try:
           return self.get_queryset().get(**kwargs)
       except self.model.DoesNotExist:
           return None


class Dialy(models.Model):

    schedule_id = models.ForeignKey(Schedule, models.CASCADE)
    user_id = models.ForeignKey(User, models.CASCADE)
    understandScore = models.IntegerField()
    comment = models.TextField(max_length=800)
    is_public = models.BooleanField(default=False)

    objects = DialyManager()

    def __str__(self):
        return str(self.user_id) + ': '+ str(self.schedule_id) + '/' + self.comment


class Message(models.Model):
    dialy = models.ForeignKey(Dialy, models.CASCADE, related_name='dialy_comment')
    user = models.ForeignKey(User, models.CASCADE)
    message = models.CharField(max_length=300)
    send_time = models.DateTimeField(default=timezone.now)