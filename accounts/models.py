from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.

def validate_phone(phone):
    if phone[:4] != '010-':
        raise ValidationError("'010-' 로 시작해주세요.")

class User(AbstractUser):

    user_auth = models.IntegerField(default=0)
    user_phone = models.CharField(max_length=20, validators=[validate_phone])
