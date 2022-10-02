# https://docs.djangoproject.com/en/4.1/topics/email/
# send_mass_mail(datatuple ,
#                fail_silently = False,
#                auth_user = None,
#                auth_password = None,
#                connection = None)
# datatuple = (subject, message, from_email, recipient_list)

# TODO: Разобраться с готовым кодом: https://github.com/pmclanahan/django-celery-email

# from django.core import mail
# from djcelery_email import tasks

# datatuple = (
#     'Test message',
#     'Test message from Django test project',
#     'alexandr_krasnot@mail.ru',
#     ['alexandr_krasnot@mail.ru'],
# )

# msg = mail.EmailMessage()
# tasks.send_email(msg, backend_kwargs={})


import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

app = Celery('django_project')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

