from django.shortcuts import render, redirect
from .models import Job,CurrentRequirement
from .forms import ApplicationForm
from django.contrib import messages
from django.views.generic import ListView,View


# Create your views here.
def home(request):
    return render(request,'career/home.html')

def about(request):

    return render(request,'career/about.html',{'title':'about'})



def jobopening(request):
    context = {
        'jobs':Job.objects.all()
    }
    return render(request,'career/openings.html',context)

def apply(request):
    
    return render(request,'career/apply.html')


class Applicationview(View):
    def get(self, *args, **kwargs):
        form = ApplicationForm()
        context = {
            'form':form
        }
        return render(self.request,'career/application.html',context)
    def post(self, *args, **kwargs):
        form  = ApplicationForm(self.request.POST or None)
        if form.is_valid():
            
            print("form is valid")
            messages.success(self.request,'Your application has been received')
            return redirect('job-application')
