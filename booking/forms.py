from django import forms
from . models import Book

class BookForm(forms.ModelForm):
    book_username = forms.CharField(
        max_length=20,
        min_length=2
    )

    book_phone = forms.CharField(
        min_length=12,
        max_length=20,
        widget= forms.TextInput(attrs={
            'placeholder' : '010-1234-5678'
        })
        
    )

    class Meta:
        model = Book
        fields = ('book_username', 'book_phone')