from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill

# Create your models here.

class HotelInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='hotel_infoes',
                             )
    
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=200, default='Hotel_Info')
    score = models.FloatField(default=0, null=True)
    price = models.PositiveIntegerField(default=0, null=True)
    image = ProcessedImageField(upload_to='images/',
                                processors=[ResizeToFill(width=600, height=600)],
                                format='JPEG'
                                )
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(width=600, height=180, upscale=False)],
                                    format='JPEG',
                                    options={'quality': 60}
                                )
    image_thumbnail_home = ImageSpecField(source='image',
                                processors=[ResizeToFill(width=800, height=200, upscale=False)],
                                format='JPEG',
                                options={'quality': 60}
                            )

def validate_score(score):
    if score < 0 and score > 5.1:
        raise ValidationError("0.0 ~ 5.0 사이의 숫자를 입력해주세요.")


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
    score = models.FloatField(default=0.0, validators=[validate_score])

class HotelProduct(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    checkin = models.DateField()
    checkout = models.DateField()
    is_booked = models.IntegerField(default=0)

    image = ProcessedImageField(upload_to='images/products/',
                                processors=[ResizeToFill(width=600, height=400)],
                                format='JPEG',
                                )
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(width=600, height=180, upscale=False)],
                                    format='JPEG',
                                    options={'quality': 60}
                                )
    image_thumbnail_profile = ImageSpecField(source='image',
                                    processors=[ResizeToFill(width=180, height=120, upscale=False)],
                                    format='JPEG',
                                    options={'quality': 60}
                                )

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