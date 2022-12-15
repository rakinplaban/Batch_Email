from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User, Email
# Register your models here.

class UserModel(ModelAdmin):
    list_display = ('id','username','email')

class Email_Display(ModelAdmin):
    list_display = ('id','subject','body','sender','timestamp')

admin.site.register(User,UserModel)
admin.site.register(Email,Email_Display)