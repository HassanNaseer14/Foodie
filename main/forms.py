from django import forms
from django.forms import ModelForm
from .models import FoodModel

class FoodForm(forms.ModelForm):
    
    class Meta:
        model = FoodModel
        fields = ("image","name")
