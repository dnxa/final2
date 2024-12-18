from django.db import models
from santaproject.santalist.models import Kid
from django.core.exceptions import ValidationError


# Create your models here.

def validate_toy_type(toy_type):
    all_kids = Kid.objects.all()

    toys_needed = [kid.gift for kid in all_kids]

    if toy_type not in toys_needed:
        raise ValidationError(f'{toy_type} is not a toy that any kid wants.')

class Toy(models.Model):
    toy_type = models.CharField(max_length=150, validators=[validate_toy_type])

class Coal(models.Model):
    pass