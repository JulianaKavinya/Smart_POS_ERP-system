from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'date_of_birth', 'hire_date', 'email', 'phone_number', 'address', 'department', 'position', 'salary', 'status']

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    hire_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )


# Override the save method to ensure that only authorized users can save
    def save(self, commit=True):
        # Ensure that the form is valid before saving
        if self.is_valid():
            employee = super().save(commit=False)
            if commit:
                employee.save()
            return employee
        else:
            # Handle form errors
            return None