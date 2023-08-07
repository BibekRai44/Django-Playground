from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'employee/index.html')

def employee(request):
    return HttpResponse("This is the employee page")
