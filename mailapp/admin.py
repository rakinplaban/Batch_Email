from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User
# Register your models here.

class UserModel(ModelAdmin):
    list_display = ('id','username','email')


admin.site.register(User,UserModel)