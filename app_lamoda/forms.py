from .models import *
from django import forms


class ReviewForms1(forms.ModelForm):
    class Meta:
        model = Review1
        fields = ['email',]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'otziv', 'placeholder': 'Email'})
        }
        labels = {
            'email': ''
        }