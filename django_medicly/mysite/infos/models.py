from django.db import models

# Create your models here.
class UserInput(models.Model):
    FirstName = models.CharField(max_length=30) #primary_key = True
    LastName = models.CharField(max_length=30)
    Gender = models.BooleanField()
    purchase_date = models.DateTimeField()
    Age = models.BigIntegerField()
    HospNumb = models.BigIntegerField()
