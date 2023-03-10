from django import forms
from .models import Text


class ModelForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = '__all__'


class NotModelForm(forms.Form):
    text = forms.CharField(min_length=1, max_length=3, required=True)
