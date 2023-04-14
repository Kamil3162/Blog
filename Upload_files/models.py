import datetime

from django.db import models
from django.contrib.auth.models import User
from datetime import timezone
'''
This file is responsible for data models like topic, etc
'''


# Create your models here.


class PostManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(title__startswith='Django')


class PostDeleter(models.Manager):
    def __init__(self, id: int):
        self.id = id

    def query_set(self):
        return super().get_queryset().delete(id=self.id)


class Id_number(models.Manager):
    def query_set(self):
        return super().get_queryset().fil


class Post(models.Model):
    # post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=500)

    objects = models.Manager()
    post_manager_django = PostManager()

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.post)


'''
class User(models.Model):
    login = models.CharField(max_length=40)
    password = models.
    def __str__(self):
        return
        '''

'''
class CustomUser(User):
    permission = models.IntegerField(blank=False)

    def __str__(self):
        return User.username
'''


class PostComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_at = models.DateField(default=datetime.datetime.now())
    
    object = models.Manager()

    def __str__(self):
        return self.user.username
