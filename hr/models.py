from django.db import models

# Employee details
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Meta:
    permissions = [
        ("view_employee", "Can view employee details"),
        ("view_sensitive_employee_data", "Can view sensitive employee data"),
        
    ]

