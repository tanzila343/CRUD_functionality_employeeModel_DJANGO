from django.shortcuts import redirect, render
from django.views import View
from .models import Employee
from .forms import AddEmployeeForm
# Create your views here.

class Home(View):
    def get(self, request):
        emp_data = Employee.objects.all()
        return render(request, 'core/home.html', {'empdata':emp_data})


class Add_Employee(View):
    def get(self, request):
        fm = AddEmployeeForm()
        return render(request, 'core/add-employee.html', {'form':fm})

    def post(self, request):
        fm = AddEmployeeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-employee.html', {'form':fm})

class Delete_Employee(View):
    def post (self, request):
        data = request.POST
        Emp_id = data.get('Emp_id')
        empdata = Employee.objects.get(Emp_id=Emp_id)
        empdata.delete()
        return redirect('/')

class EditEmployee(View):
    def get(self, request, Emp_id):
        emp = Employee.objects.get(Emp_id=Emp_id)
        fm = AddEmployeeForm(instance=emp)
        return render(request, 'core/edit-employee.html', {'form':fm})

    def post(self, request, Emp_id):
        emp = Employee.objects.get(Emp_id=Emp_id)
        fm = AddEmployeeForm(request.POST, instance=emp)
        if fm.is_valid():
            fm.save()
            return redirect('/')
            