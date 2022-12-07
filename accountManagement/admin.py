from django.contrib import admin
from .models import Traineer, Company, ITLGroup, ITLGroupUser
# Register your models here.

#class TraineerForeignKeyModelInLine(admin.TabularInline):
#    model = Traineer

class TraineerAdmin(admin.ModelAdmin):
    list_display = ('id','traineer','company')
    #inlines = [TraineerForeignKeyModelInLine]

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class ITLGroupAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')

class ITLGroupUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group')

admin.site.register(Traineer, TraineerAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(ITLGroup, ITLGroupAdmin)
admin.site.register(ITLGroupUser, ITLGroupUserAdmin)
