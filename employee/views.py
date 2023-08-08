from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'base.html')

def employee(request):
    if request.method=='POST':
        data=request.POST
        email=data.get('email')
        password=data.get('password')
        context={
           'email':email,
           'password':password
       }
    else:
        context={
            'name':'Bibek Rai',
            'address':'Biratnagar'
        }
    return render(request,'employee/employee.html',context)


