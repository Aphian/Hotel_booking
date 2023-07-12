from django import forms
from . models import HotelInfo, HotelReviews, HotelProduct

class HotelInfoForm(forms.ModelForm):
    name = forms.CharField(
        min_length=2,
        max_length=30,
    )

    info = forms.CharField(
        max_length=200,
        min_length=2,
        widget=forms.Textarea()
    )

    class Meta:
        model = HotelInfo
        exclude = ('user', 'score', 'price', )

class HotelReviewForm(forms.ModelForm):
    content = forms.CharField(
        min_length=2,
        max_length=200,
        label='Review',
        widget=forms.Textarea(),
    )

    score = forms.FloatField(
        min_value=0.0,
        max_value=5.0,
        widget=forms.TextInput(attrs={
            'placeholder' : '0.0 ~ 5.0',
        })
    )

    class Meta:
        model = HotelReviews
        fields = ('content', 'score', )

class HotelProductForm(forms.ModelForm):
    title = forms.CharField(
        min_length=2,
        max_length=30,
    )

    price = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput()
    )

    checkin = forms.DateField(
        widget= forms.DateInput(attrs={
            'placeholder' : '2023-01-01',
        })
    )

    checkout = forms.DateField(
        widget= forms.DateInput(attrs={
            'placeholder' : '2023-01-01',
        })
    )

    class Meta:
        model = HotelProduct
        fields = ('title', 'price', 'checkin', 'checkout', )