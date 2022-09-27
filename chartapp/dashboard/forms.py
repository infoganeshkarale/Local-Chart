from django import forms
from .models import PMSData

class PMSDataFrom(forms.ModelForm):
    class Meta:
        model = PMSData
        fields = '__all__'
