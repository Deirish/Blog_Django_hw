from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Post(models.Model):
    author = models.ManyToManyField(User)
    topic = models.ManyToManyField(Topic)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text
