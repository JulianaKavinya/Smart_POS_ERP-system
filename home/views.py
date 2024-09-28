from django.shortcuts import render

from django.template import engines

def landing_page(request):
    return render(request, 'home/landing_page.html')

def dashboard(request):
    return render(request, 'inventory/dashboard.html')