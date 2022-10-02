from django.contrib import admin
from .models import Post
from . import tasks

admin.site.register(Post)

def send(modeladmin, request):
    tasks.send_email.delay()
    
send.short_description = "send"