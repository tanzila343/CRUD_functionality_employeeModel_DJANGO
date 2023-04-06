from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_id = models.IntegerField(unique=True)
    Emp_Name = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
