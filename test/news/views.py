from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from rest_framework.parsers import MultiPartParser, FormParser

from news.serializers import PostSerializer, UserSerializer, GroupSerializer
from .models import Post
from .tasks import send_email


class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PostSerializer

