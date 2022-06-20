from django.contrib import admin
from user.models import User, Staff

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','__str__', 'email', 'is_active')
    #list_editable = ('is_active')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id','__str__', 'email', 'is_active', 'is_traineer')
    #list_editable = ('is_active', 'is_staff', 'is_traineer')


admin.site.register(User, UserAdmin)
admin.site.register(Staff, StaffAdmin)

