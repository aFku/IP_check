from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    publish_date = models.DateTimeField(default=timezone.now)
