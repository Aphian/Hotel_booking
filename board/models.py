from django.db import models
from django.conf import settings

# Create your models here.

class AdminBoard(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)