from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    joined_at = models.DateTimeField(default=datetime.datetime.now)
    is_authenticated = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
