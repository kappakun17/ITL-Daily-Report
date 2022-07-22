from django.contrib import admin
from .models import Category, Training, Schedule, TrainingTraineer
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category')

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'company')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'training', 'staff_memo','traineer_memo','start_time', 'end_time')
    #inlines = [TrainingForeignKeyModelInLine]

class TrainingTraineerAdmin(admin.ModelAdmin):
    list_display = ('id', 'training', 'traineer')
    #inlines = [TrainingForeignKeyModelInLine]

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Training,TrainingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TrainingTraineer, TrainingTraineerAdmin)
