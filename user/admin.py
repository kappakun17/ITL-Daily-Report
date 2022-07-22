from django.contrib import admin
from user.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','__str__', 'email', 'is_active','is_activated','is_staff','is_traineer','date_joined')
    #list_editable = ('is_active')



admin.site.register(User, UserAdmin)


