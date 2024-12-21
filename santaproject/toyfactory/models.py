from django.db import models
from santalist.models import Kid

class Toy(models.Model):
    toy_type = models.CharField(max_length=150)

    owner = models.ForeignKey(Kid, on_delete=models.CASCADE, null=True, blank=True, related_name='toys')

    # In minutes
    time_to_make = models.IntegerField()

    def __str__(self):
        return str(self.toy_type)

class Coal(models.Model):
    owner = models.ForeignKey(Kid, on_delete=models.CASCADE, null=True, blank=True, related_name='coals')
