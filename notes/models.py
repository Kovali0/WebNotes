from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class Topic(TitleSlugDescriptionModel, TimeStampedModel):
    pass


class Note(TimeStampedModel):
    title = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)