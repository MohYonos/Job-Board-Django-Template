from django.db import models


# Create your models here.

JOB_TYPE = [
    ('FULL TIME','FULL TIME'),
    ('PART TIME','PART TIME'),
    ('FREELANCER','FREELANCER'),
]
 

class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=2000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experinces = models.IntegerField(default=1)
    category = models.ForeignKey('Categort', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Categort(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name