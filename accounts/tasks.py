# from celery import shared_task
# from django.conf import settings
# from django.core.mail import send_mail
#
#
# @shared_task
# def send_welcome_email(email):
#     send_mail(
#         subject='Welcome to WorkoutLab!',
#         message='We are thrilled to have you with us!',
#         from_email=settings.COMPANY_EMAIL,
#         recipient_list=[email],
#         fail_silently=True
#     )


#issues with setting redis cache on azure. webjob can't run