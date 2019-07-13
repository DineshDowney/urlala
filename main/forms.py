from django import forms
from main.models import shorted_urls

class FormClass(forms.ModelForm):
    class Meta:
        model = shorted_urls
        fields = ['long_urls',]
