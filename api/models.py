from django.db import models
from django.contrib.auth.models import User
import datetime

class Movies(models.Model):
    id = models.IntegerField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    url_path = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    duration = models.IntegerField()
    updated = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    movies = models.ForeignKey(Movies, on_delete = models.CASCADE)
    text = models.TextField(null = True, blank = True)

class React(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    movies = models.ForeignKey(Movies, on_delete = models.CASCADE)

class Share(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    movies = models.ForeignKey(Movies, on_delete = models.CASCADE)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    movies = models.ForeignKey(Movies, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)