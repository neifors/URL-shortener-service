from .models import Equivalent
from django import forms

class NewShortUrlForm(forms.ModelForm):
    class Meta:
        model = Equivalent
        fields = ['original']
        labels = {'original': 'URL'}
