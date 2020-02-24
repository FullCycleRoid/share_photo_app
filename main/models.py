import uuid

from django.conf import settings
from django.db import models


# Create your models here.


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, default='Untitled')
    url = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d')
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_photo')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
