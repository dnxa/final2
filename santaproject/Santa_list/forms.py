from django import forms
from .models import Kid, SantasList

class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['first_name', 'last_name', 'niceness_coefficient', 'gift']

class KidDeleteForm(forms.Form):
    kid_id = forms.IntegerField()
