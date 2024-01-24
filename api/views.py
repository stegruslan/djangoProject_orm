from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView, RetrieveAPIView)
from api.models import User, Post, Comment
from api.serializers import UserSerializer, PostSerializer, CommentSerializer


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
