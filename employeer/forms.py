from django import forms

class EmployeerForm(forms.Form):
    name=forms.CharField(max_length=150)
    email=forms.EmailField(max_length=150)