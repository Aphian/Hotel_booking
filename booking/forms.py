from django import forms
from . models import Book

class BookForm(forms.ModelForm):
    name = forms.CharField(
        max_length=20,
        min_length=2
    )

    phone = forms.CharField(
        min_length=13,
        max_length=20,
        widget= forms.TextInput(attrs={
            'placeholder' : '010-1234-5678'
        })
        
    )

    class Meta:
        model = Book
        fields = ('name', 'phone', )