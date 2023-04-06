from django import forms
from .models import Employee

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("Emp_id","Emp_Name","Dept")
        widgets = {
            'Emp_id': forms.NumberInput(attrs={'class':'form-control'}),
            'Emp_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Dept': forms.TextInput(attrs={'class':'form-control'}),
        }