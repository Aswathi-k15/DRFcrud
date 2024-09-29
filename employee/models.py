from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return f"{self.employee_name} "