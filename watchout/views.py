from django.shortcuts import render
from .models import Employees

def login(request):
    employee = Employees.objects.get(emp_id="2013130141")
    return render(request, 'watchout/login.html',{'employee':employee})

def emphome(request):
    return render(request, 'watchout/emp_home.html', {})

def timeleft(request):
    return render(request, 'watchout/timeleft.html', {})

def logusers(request):
    emp = Employees.objects.all()
    return render(request, 'watchout/logusers.html',{'emp':emp})
