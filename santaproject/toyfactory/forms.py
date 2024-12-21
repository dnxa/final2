from django import forms
from .models import Toy, Coal
from santalist.models import Kid
from django.core.exceptions import ValidationError


class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['toy_type', 'time_to_make']

    def clean_toy_type(self):
        toy_type = self.cleaned_data['toy_type']

        toy_needed = Kid.objects.filter(gift=toy_type).exists()

        if not toy_needed:
            raise ValidationError(f'{toy_type} is not a toy that any kid wants.')

        return toy_type

