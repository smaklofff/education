from .models import *
from django.forms import ModelForm, TextInput


class Filters(ModelForm):
    class Meta:
        model = Lego
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название набора'
            })
        }
