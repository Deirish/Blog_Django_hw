from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Topic(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Topic')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Post(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    author = models.ManyToManyField(User)
    title = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    visible = models.BooleanField(default=1)
    publish = models.DateTimeField(default=timezone.now)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['title']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def get_absolute_url(self):
        return reverse('comment', kwargs={'comment_slug': self.slug})

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return '{}'.format(self.author)


class PersonalPage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


