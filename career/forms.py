from django import forms
from .models import Job,CurrentRequirement

class ApplicationForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    skill1 = forms.CharField(label='skill1', max_length=100)
    skill2 = forms.CharField(label='skill2', max_length=100)
    skill3 = forms.CharField(label='skill3', max_length=100)
    experience = forms.IntegerField(label='Experience')
    location = forms.CharField(label='Location', max_length=100)

    
            