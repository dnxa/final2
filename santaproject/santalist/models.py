from django.db import models

# Create your models here.
class Kid(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    niceness_coefficient = models.DecimalField(max_digits=3, decimal_places=2)
    gift = models.CharField(max_length=150)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SantasList(models.Model):
    naughty_list = models.ManyToManyField(Kid, related_name="naughty_lists", blank=True)
    nice_list = models.ManyToManyField(Kid, related_name="nice_list", blank=True)