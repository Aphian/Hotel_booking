from django.db import models
from django.conf import settings

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    state = models.IntegerField(default=0)
    phone = models.CharField(max_length=13)
    use_date = models.CharField(max_length=20)

    # 상품 번호 외래키 모델링
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='book_user')
