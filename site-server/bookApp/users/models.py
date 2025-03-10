from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True)