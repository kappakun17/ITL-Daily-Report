from django.contrib import admin
from .models import Dialy, Message

# Register your models here.

class DialyAdmin(admin.ModelAdmin):
    list_display = ('id','user_id', 'schedule_id', 'understandScore', 'comment', 'is_public')

class MessageAdmin(admin.ModelAdmin):
	list_display = ('id', 'dialy', 'user', 'message', 'send_time')

admin.site.register(Dialy, DialyAdmin)
admin.site.register(Message, MessageAdmin)