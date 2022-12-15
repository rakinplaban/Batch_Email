from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.email

class Email(models.Model):
    subject = models.CharField(max_length=100)
    # body = RichTextField()
    body = RichTextUploadingField(blank=True,null=True)
    sender = models.ForeignKey(User, on_delete=CASCADE,related_name='sender')
    timestamp = datetime.now()
    