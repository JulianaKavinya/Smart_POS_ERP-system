from django.shortcuts import render,get_object_or_404,redirect
from .models import Employee
from .forms import EmployeeForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required



# View to display the list of employees
@login_required  # Ensure only logged-in users can access the employee list
def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'hr/employee_list.html', {'employees': employees})


# View to display employee details with permission check
@permission_required('hr.view_employee', raise_exception=True)  # Ensure user has 'view_employee' permission
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)  # Fetch the employee object or return 404 if not found
    return render(request, 'hr/employee_detail.html', {'employee': employee})


# View to handle adding a new employee
@login_required  # Ensure only logged-in users can add employees
@permission_required('hr.add_employee', raise_exception=True)  # Check for 'add_employee' permission
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)  # Process the form data
        if form.is_valid():
            form.save()  # Save the new employee to the database
            return redirect('employee_list')  # Redirect to employee list after successful submission
        else:
            print(form.errors)  # Log or display form errors for debugging
    else:
        form = EmployeeForm()  # Display a blank form for GET requests
    return render(request, 'hr/add_employee.html', {'form': form})


# View to handle editing an employee's details
@login_required  # Ensure only logged-in users can edit employees
@permission_required('hr.change_employee', raise_exception=True)  # Check for 'change_employee' permission
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)  # Fetch the employee object or return 404 if not found
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)  # Bind the form to the existing employee
        if form.is_valid():
            form.save()  # Save the updated employee to the database
            return redirect('employee_detail', pk=employee.pk)  # Redirect to employee detail after successful edit
        else:
            print(form.errors)  # Log or display form errors for debugging
    else:
        form = EmployeeForm(instance=employee)  # Display the form with existing employee data
    return render(request, 'hr/edit_employee.html', {'form': form})


# View to handle deleting an employee
@login_required  # Ensure only logged-in users can delete employees
@permission_required('hr.delete_employee', raise_exception=True)  # Check for 'delete_employee' permission
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)  # Fetch the employee object or return 404 if not found
    if request.method == 'POST':
        employee.delete()  # Delete the employee from the database
        return redirect('employee_list')  # Redirect to employee list after deletion
    return render(request, 'hr/confirm_delete.html', {'employee': employee})  # Render a confirmation page


# Custom 403 Forbidden handler for unauthorized access attempts (optional)
def custom_403_view(request, exception=None):
    return render(request, '403.html', status=403)  # Render a custom 403 error page
