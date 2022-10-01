from django.urls import path

# from symbol import parameters
from .views import PostList, PostDetail, UserViewSet, GroupViewSet

urlpatterns = [
    path('users/<int:pk>/', UserViewSet.as_view()),
    path('users/', GroupViewSet.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]
