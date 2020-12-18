from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey( User, on_delete=models.CASCADE ) #default = User.objects.get(id=1).pk