from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
# Create your views here.

def index(request):
    return render(request,'base.html')

def employee(request):
    if request.method=='POST':
        # data=request.POST
        # email=data['email']
        # name=data['name']
        # context={
        #    'name':name,
        #    'email':email 
        # }
        pass
    else:
        form=EmployeeForm()
        context={
            'form':form
            
        }
    return render(request,'employee/employee.html',context)


