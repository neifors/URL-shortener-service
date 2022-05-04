from django.db import models

# Create your models here.
class Equivalent(models.Model):
   alias = models.CharField(max_length=100)
   original = models.CharField(max_length=250)
   
   
   def __str__(self):
       return f"{self.alias} ({self.original})"
