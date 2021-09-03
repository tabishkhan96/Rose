from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=4, decimal_places=4)
    material = models.CharField(max_length=100)
    pics = models.FileField(upload_to='static/', max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

