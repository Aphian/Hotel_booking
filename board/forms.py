from django import forms
from . models import AdminBoard

class AdminBoardForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        min_length=2,
    )

    content = forms.CharField(
        max_length=2,
        widget=forms.Textarea()
    )

    class Meta:
        model = AdminBoard
        field = ['title', 'content']