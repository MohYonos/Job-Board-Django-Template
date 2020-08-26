from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.AllJobs),
    path('<int:id>', views.JobDetails),
]