"""Models file"""
from django.db import models

# Create your models here.


class Pet(models.Model):
    """Creating Pet database"""
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200, default="")
    age = models.IntegerField()
    description = models.CharField(max_length=400, default="")
    image = models.ImageField(upload_to='images/', blank = True, null = True)

    def __str__(self):
        return self.name  + " "
