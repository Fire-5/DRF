from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    def upload_to(instance, filename):
        return f'images/{filename}'

    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
