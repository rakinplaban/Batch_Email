from celery import shared_task
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from .models import User

@shared_task(bind=True)
def send_mail_func(self,subject,body,sender):
    users = User.objects.all()
    receipents = []
    for user in users:
        receipents.append(user.email)
    # send_mail(
    #     subject,body,sender,receipents, 
    #     fail_silently=False
    # )
    msg = EmailMultiAlternatives(subject,body,sender,receipents)
    msg.attach_alternative(body, "text/html")
    msg.send()
    return "Done!"