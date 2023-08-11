from django.forms import ModelForm
from .models import Person
from django import forms

class EmployeeForm(ModelForm):
    address=forms.CharField(max_length=120)
    class Meta:
        model=Person
        fields=['first_name','last_name','address']