from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from hotel_booking.models import HotelProduct
from booking.models import Book

def validate_phone(phone):
    if phone[:4] != '010-':
        raise ValidationError("'010-' 로 시작해주세요.")

class User(AbstractUser):

    name = models.CharField(max_length=10, blank=True)
    # user_auth = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    phone = models.CharField(max_length=20, validators=[validate_phone])

    # User : HotelProduct = M : N
    reserved_products = models.ManyToManyField(HotelProduct, through=Book, related_name='reserved_users')