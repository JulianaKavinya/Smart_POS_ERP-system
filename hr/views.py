from django.shortcuts import render,get_object_or_404,redirect
from .models import Employee
from .forms import EmployeeForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


def employee_list(request):
    employees = Employee.objects.all()
    #print(employees)
    return render(request, 'hr/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hr/employee_detail.html', {'employee': employee})

# View to handle adding a new employee
def add_employee(request):
    if request.method == 'POST':
        # If the request is a POST, process the form data
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the new employee to the database
            form.save()
            # Redirect to the employee list page after successful submission
            return redirect('employee_list')
        else:
            # Print or log form errors for debugging
            print(form.errors)
    else:
        # If the request is GET, display a blank form
        form = EmployeeForm()
        # Render the template with the form
    return render(request, 'hr/add_employee.html', {'form': form})


# Decorator to ensure that only logged-in users can access this view
@login_required
def employee_detail(request, pk):
    # Fetch the employee object or return a 404 if not found
    employee = get_object_or_404(Employee, pk=pk)
    
    # Check if the user has permission to view the employee details
    if request.user.has_perm('hr.view_employee', employee):
        # Render the employee details template if user has permission
        return render(request, 'hr/employee_detail.html', {'employee': employee})
    else:
        # Render a forbidden page if user does not have permission
        return render(request, '403.html')  # Custom 403 Forbidden page
    

    # Decorator to ensure that the user has the 'view_employee' permission
@permission_required('hr.view_employee', raise_exception=True)
def employee_detail(request, pk):
    # Fetch the employee object or return a 404 if not found
    employee = get_object_or_404(Employee, pk=pk)
    
    # Render the employee details template since the user has permission
    return render(request, 'hr/employee_detail.html', {'employee': employee})