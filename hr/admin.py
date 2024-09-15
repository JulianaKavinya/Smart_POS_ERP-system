from django.contrib import admin

# Registering my models here.
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'position', 'hire_date', 'status')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'status')
