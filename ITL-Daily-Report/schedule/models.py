from django.db import models
from accountManagement.models import Company, Traineer, ITLGroup


# Create your models here.

class ScheduleManager(models.Manager):
    def get_or_none(self, **kwargs):
       
       try:
           return self.get_queryset().get(**kwargs)
       except self.model.DoesNotExist:
           return None


class Category(models.Model):
    category = models.CharField('category', max_length=200)

    def __str__(self):
        return self.category

class Training(models.Model):

    title = models.CharField('title' ,max_length=250)
    description = models.TextField('description',max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(ITLGroup, on_delete=models.SET_DEFAULT, default=0)
    company = models.ForeignKey(
        Company, 
        on_delete=models.SET_DEFAULT,
        default='no-company'
        )


    def __str__(self):
        return '{}/{}'.format(self.title, self.company)

class Schedule(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    staff_memo = models.TextField('staff memo', max_length=500, blank=True, null=True)
    traineer_memo = models.TextField('traineer memo', max_length=500, blank=True, null=True)

    start_time = models.DateTimeField('date')
    end_time = models.DateTimeField('end time')

    objects = ScheduleManager()

    def __str__(self):
        return str(self.id)


class TrainingTraineer(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    traineer = models.ForeignKey(Traineer,on_delete=models.CASCADE)



