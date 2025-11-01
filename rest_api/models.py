from django.db import models

# Create your models here.

class Student(models.Model):
   name = models.CharField(max_length=100)
   age = models.IntegerField(blank=True, null=True)
   department = models.CharField(max_length=100, blank=True, null=True)