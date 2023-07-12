from django.contrib import admin
from . models import HotelInfo, HotelProduct, HotelReviews

# Register your models here.


admin.site.register(HotelInfo)
admin.site.register(HotelProduct)
admin.site.register(HotelReviews)