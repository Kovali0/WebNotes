from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from mptt.models import MPTTModel, TreeForeignKey


class Topic(MPTTModel, TitleSlugDescriptionModel, TimeStampedModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
    is_public = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['title']


class Note(TimeStampedModel):
    title = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)