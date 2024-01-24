from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=50)
    registration = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Comment(models.Model):
    text = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
