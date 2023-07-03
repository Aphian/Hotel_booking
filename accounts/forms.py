from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    user_phone = forms.CharField(
        min_length=12,
        max_length=20,
        widget= forms.TextInput(attrs={
            'placeholder' : '010-1234-5678'
        })
        
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'user_phone', )