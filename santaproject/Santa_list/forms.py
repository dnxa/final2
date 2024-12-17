from django import forms
from .models import Kid

class KidForm(forms.ModelForm):
    class Meta:
        Model = Kid
        fields = ['first_name', 'last_name', 'niceness_coefficient', 'gift']