from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def send_email(msg):
    subject = 'test head'
    message = 'test msg'
    mail_sent = send_mail(subject,
                          message,
                          'alexandr_krasnot@mail.ru',
                          ['alexandr_krasnot@mail.ru'])
    return mail_sent