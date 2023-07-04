from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.

class HotelInfo(models.Model):
    hotel_name = models.CharField(max_length=100)
    # hotel_image = models.ImageField(blank= True, upload_to = 'images/')
    hotel_price = models.CharField(max_length=15)
    hotel_checkin = models.CharField(max_length=12)
    hotel_checkout = models.CharField(max_length=12)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='hotel_infoes',
                             )

class HotelReviews(models.Model):
    review_content = models.CharField(max_length=200)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               )
    hotel_info = models.ForeignKey(HotelInfo,
                                   on_delete=models.CASCADE,
                                   related_name='reviews',
                                   )
