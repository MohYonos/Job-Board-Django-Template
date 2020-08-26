from django.contrib import admin

# Register your models here.
from .models import Job , Categort

admin.site.register(Job)
admin.site.register(Categort)