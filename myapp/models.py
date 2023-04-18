from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


class Topic(models.Model):
    author = models.ManyToManyField(User, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    discription = models.TextField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)



