from django.db import models
from django.core.exceptions import ValidationError
from santalist.models import Kid

# Create your models here.

# Not used just here for migrations to not give an error
def validate_toy_type(toy_type):
    all_kids = Kid.objects.all()

    toys_needed = [str(kid.gift) for kid in all_kids]
    print(all_kids)
    if str(toy_type) not in toys_needed:
        raise ValidationError(f'{toy_type} is not a toy that any kid wants.')

class Toy(models.Model):
    toy_type = models.CharField(max_length=150)

    owner = models.ForeignKey(Kid, on_delete=models.CASCADE, null=True, blank=True, related_name='toys')

    # In minutes
    time_to_make = models.IntegerField()

    def __str__(self):
        return str(self.toy_type)

class Coal(models.Model):
    owner = models.ForeignKey(Kid, on_delete=models.CASCADE, null=True, blank=True, related_name='coals')
