from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def dashboard(request):
    return render(request, 'inventory/dashboard.html')


from django.http import HttpResponse

def inventory_home(request):
    return HttpResponse("Welcome to the Inventory app!")

