from django.db import models
from django.utils import timezone
# from .forms import ApplicationForm

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        
class CurrentRequirement(models.Model):
    skill1 = models.CharField( max_length=100)
    skill2 = models.CharField( max_length=100)
    skill3 = models.CharField( max_length=100)
    experience = models.IntegerField()
    location = models.CharField( max_length=100)

    # def match(self):
    #     requirements = ['skill1','skill2 ','skill3','experience','location']
    #     inputs = ApplicationForm.objects.all()
    #     if 