from django import forms
from . models import HotelInfo, HotelReviews

class HotelInfoForm(forms.ModelForm):
    hotel_name = forms.CharField(
        min_length=2,
        max_length=30,
    )

    hotel_price = forms.CharField(
        min_length=0,
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder' : '1,000,000',
        })
    )

    hotel_image = forms.CharField(
        max_length=100,
        min_length=0,
    )

    hotel_checkin = forms.DateField(
        widget= forms.DateInput(attrs={
            'placeholder' : '2023-01-01',
        })
    )

    hotel_checkout = forms.DateField(
        widget= forms.DateInput(attrs={
            'placeholder' : '2023-01-01',
        })
    )

    hotel_info = forms.CharField(
        max_length=200,
        min_length=2,
        widget=forms.Textarea()
    )

    class Meta:
        model = HotelInfo
        exclude = ['user', ]

class HotelReviewForm(forms.ModelForm):
    review_content = forms.CharField(
        min_length=2,
        max_length=200,
        widget=forms.Textarea()
    )

    review_score = forms.FloatField(
        min_value=0.0,
        widget=forms.Textarea(attrs={
            'placeholder' : '0.0 ~ 5.0',
        })
    )

    class Meta:
        model = HotelReviews
        fields = ['review_content', 'review_score']