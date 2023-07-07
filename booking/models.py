from django.db import models
from django.conf import settings

from hotel_booking.models import HotelProduct
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    state = models.IntegerField(default=0)
    phone = models.CharField(max_length=13)

    # 상품 번호 외래키 모델링
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='books')
    
    product = models.ForeignKey(HotelProduct,
                                on_delete=models.CASCADE,
                                related_name='books',)
