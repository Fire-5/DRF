from celery import shared_task
from django.core import mail

@shared_task
def send_email():
    subject = 'test head'
    message = 'test msg by django app'
    mail_sent = mail.send_mass_mail(subject,
                                    message,
                                    'alexandr_krasnot@mail.ru',
                                    ['alexandr_krasnot@mail.ru'])
    return mail_sent

