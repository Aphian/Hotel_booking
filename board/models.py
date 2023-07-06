from django.db import models
from django.conf import settings

# Create your models here.

class AdminBoard(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='admin_author'
                             )