from django import forms
from .models import Toy, Coal

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['toy_type']