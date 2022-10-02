from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# Как в книжке не сработало, переделал по аналогии с группами юзеров - получилось.
# class PostSerializer(serializers.ModelSerializer):
#     model = Post
#     fields = ['id', 'title', 'text', 'author', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'author', 'image_url', 'created_at']

