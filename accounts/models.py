from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    user_auth = models.IntegerField(default=0)
    user_phone = models.CharField(max_length=20)
