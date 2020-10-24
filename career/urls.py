from django.urls import path
from . import views
from .views import Applicationview

urlpatterns = [
    path('', views.home, name = 'job-home'),
    path('about/', views.about, name = 'job-about'),
    path('jobopening/', views.jobopening, name = 'job-openings'),
    path('apply/', views.apply, name = 'job-apply'),
    path('application/', views.Applicationview.as_view(), name = 'job-application')
]
