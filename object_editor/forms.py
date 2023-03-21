from django import forms
from .models import TextObject


class TextForm(forms.ModelForm):
    class Meta:
        model = TextObject
        fields = '__all__'
