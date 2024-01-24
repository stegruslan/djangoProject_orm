from collections import UserList

from django.urls import path
from api.views import *

urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('users/create/', UserCreateAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
    path('posts/', PostListAPIView.as_view()),
    path('posts/create/', PostCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
    path('comments/', CommentListAPIView.as_view()),
    path('comments/create/', CommentCreateAPIView.as_view()),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view())
]