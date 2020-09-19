from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    user_bio = models.TextField(default="")
    bio_pic = models.URLField(default="")
    date_joined = models.DateField(default=datetime.datetime.now())
    project_owner = models.BooleanField(default=True)

    def __str__(self):
        return self.username