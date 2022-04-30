from rest_framework import serializers

from .models import jobseeker_model,jobrecruiter_model,jobs_model

class log_jobseeker_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = jobseeker_model
        fields = ['name','email','dob','mobile','degree','pwsd','passed_out_year','percentile','experience','applied_job','applied_company']
        
class log_jobrecruiter_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = jobrecruiter_model
        fields = ['name','email','mobile','pwsd','company_name','company_desc']
        
class log_jobsmodel_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = jobs_model
        fields = ['job_title','job_description','job_skills','job_experiance','job_company_name','job_company_email']