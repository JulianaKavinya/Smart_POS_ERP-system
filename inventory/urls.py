from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
     path('', views.inventory_home, name='inventory_home'),

]
