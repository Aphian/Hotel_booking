from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.

class HotelInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='hotel_infoes',
                             )
    
    name = models.CharField(max_length=100)
    # hotel_image = models.ImageField(blank= True, upload_to = 'images/')
    image = models.CharField(max_length=100)
    info = models.CharField(max_length=200, default='Hotel_Info')
    score = models.FloatField(default=0, null=True)
    price = models.PositiveIntegerField(default=0, null=True)


class HotelReviews(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               )
    
    info = models.ForeignKey(HotelInfo,
                            on_delete=models.CASCADE,
                            related_name='reviews',
                            )
    
    content = models.CharField(max_length=200)
    score = models.FloatField(default=0.0)

class HotelProduct(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    checkin = models.DateField()
    checkout = models.DateField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='reservation',
                             )

    info = models.ForeignKey(HotelInfo,
                             on_delete=models.CASCADE,
                             related_name='products',
                             )
    
if __name__ == '__main__':

    pass
