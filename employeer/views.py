from django.http import HttpResponse
from django.shortcuts import render

def employeer(request):
    data=request.POST
    #print(data.get('email'))
    #print(data.get('password'))
    return render(request,'employeer/employeer.html')