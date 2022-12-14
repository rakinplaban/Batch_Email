from celery import shared_task
from django.core.mail import send_mail
from .models import User

@shared_task(bind=True)
def send_mail_func(self,subject,body):
    users = User.objects.all()
    receipents = []
    for user in users:
        receipents.append(user.email)
    send_mail(
        subject,body,'plaban_r@yahoo.com',receipents, 
        fail_silently=False
    )
    return "Done!"