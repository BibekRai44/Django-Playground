from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeerForm

def employeer(request):
        if request.method == 'POST':
            form=EmployeerForm(request.POST)
            print(form.is_valid())
            data=form.cleaned_data
            print(data['name'])
            print(data['email'])
        form=EmployeerForm()
        context={
            'form':form
        }
        return render(request,'employeer/employeer.html',context)