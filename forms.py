from django import forms
from productdetails.models import product

class pdforms(forms.ModelForm):
    class Meta:
        model=product
        fields="__all__"
