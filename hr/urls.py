

from django.urls import path
from . import views

app_name = 'hr'  

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),#<int:pk>means real interger like 1,2 etc
    path('add/', views.add_employee, name='add_employee'),  # URL pattern for adding a new employee
    path('dashboard/', views.dashboard, name='dashboard'),

]
