from django.urls import path
from .views import Home, Add_Employee, Delete_Employee, EditEmployee
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-employee/', Add_Employee.as_view(), name='add-employee'),
    path('delete-employee/', Delete_Employee.as_view(), name='delete-employee'),
    path('edit-employee/<int:Emp_id>/', EditEmployee.as_view(), name='edit-employee')
]