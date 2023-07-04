from django import forms
from . models import HotelInfo, HotelReviews

class Hotel_Info_Form(forms.ModelForm):
    hotel_name = forms.CharField(
        min_length=2,
        max_length=30,
    )

    hotel_price = forms.CharField(
        min_value=0,
        max_value=15,
        widget=forms.Textarea(attrs={
            'placeholder' : '1,000,000',
        })
    )

    class Meta:
        model = HotelInfo
        exclude = ['user', ]

class Hotel_Review_Form(forms.ModelForm):

    class Meta:
        model = HotelReviews
        field = ['review_content', ]