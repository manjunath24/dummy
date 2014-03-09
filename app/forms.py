from django import forms
from .models import Institute


class InstituteRegForm(forms.ModelForm):
    class Meta:
        model = Institute
        exclude = ('id', 'is_active')