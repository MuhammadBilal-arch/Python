# models.py
from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    age = models.IntegerField()