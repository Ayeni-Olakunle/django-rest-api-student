from enum import auto
from unicodedata import name
from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
