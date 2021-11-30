from django.db import models

class Employee(models.Model):
    name = models.CharField(null=False, max_length=512)
    surname = models.CharField(null=False, max_length=512)
    salary = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    birth_date = models.DateField(null=False)