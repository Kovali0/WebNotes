from django.db import models
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )