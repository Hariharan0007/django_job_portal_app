from django.contrib import admin

# Register your models here.

from .models import jobseeker_model,jobrecruiter_model,jobs_model

admin.site.register(jobseeker_model)
admin.site.register(jobrecruiter_model)
admin.site.register(jobs_model)