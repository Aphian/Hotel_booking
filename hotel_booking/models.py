from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.

class HotelInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='hotel_infoes',
                             )
    
    hotel_name = models.CharField(max_length=100)
    # hotel_image = models.ImageField(blank= True, upload_to = 'images/')
    hotel_image = models.CharField(max_length=100)
    hotel_price = models.CharField(max_length=15)
    hotel_checkin = models.DateField()
    hotel_checkout = models.DateField()
    hotel_info = models.CharField(max_length=200, default='Hotel_Info')


class HotelReviews(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               )
    hotel_info = models.ForeignKey(HotelInfo,
                                   on_delete=models.CASCADE,
                                   related_name='reviews',
                                   )
    
    review_content = models.CharField(max_length=200)
    review_score = models.FloatField(default=0.0)

