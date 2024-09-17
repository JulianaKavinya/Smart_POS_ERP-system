from django.shortcuts import render,get_object_or_404

# Creating my views here

from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    #print(employees)
    return render(request, 'hr/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hr/employee_detail.html', {'employee': employee})

