from django.http import HttpResponse
from django.shortcuts import render

def employeer(request):
    return render(request,'employeer/employeer.html')