import threading
from django.core.mail import send_mail
from django.conf import settings


def send_welcome_email(email):
    send_mail(
        subject='Welcome to WorkoutLab',
        message='We are thrilled to have you with us!',
        from_email=settings.COMPANY_EMAIL,
        recipient_list=[email],
        fail_silently=True)


def send_welcome_email_async(user_email):
    threading.Thread(
        target=send_welcome_email,
        args=(user_email,),
        daemon=True
    ).start()