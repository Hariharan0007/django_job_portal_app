from django.db import models

# Create your models here.

class jobseeker_model(models.Model):     # Jobseeker Registration
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,primary_key=True)
    dob = models.DateField(max_length=20)
    mobile = models.IntegerField()
    pwsd = models.CharField(max_length=50)
    repwsd = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    passed_out_year = models.DateField(max_length=20)
    percentile = models.IntegerField()
    experience = models.IntegerField()
    #applied_job = models.CharField(max_length=100)
    #applied_company = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + ' ' + self.email
        

class jobrecruiter_model(models.Model): # JobRecruiter Registration
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,primary_key=True)
    mobile = models.IntegerField()
    pwsd = models.CharField(max_length=50)
    repwsd = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    company_desc = models.CharField(max_length=100)
    
    def __str__(self):
        return self.company_name +' ' + self.name + ' ' + self.email
    
    
class jobs_model(models.Model):
    class Meta:
        unique_together=(('job_title','job_company_name'),) #composite key
    job_title = models.CharField(max_length=100,)
    job_description = models.CharField(max_length=100)
    job_skills = models.CharField(max_length=150)
    job_experiance = models.IntegerField()
    job_company_name = models.CharField(max_length=50)
    job_company_email = models.EmailField(max_length=50)
    no_of_openings = models.IntegerField()
    def __str__(self):
        return self.job_company_name +' ' + self.job_title + ' ' + self.job_company_email
    
    
class job_apply_model(models.Model):

    class Meta:
        unique_together = (('id','job_company_email'),)
    job_title = models.CharField(max_length=100) # primary_key to avoid duplicate
    job_company_email = models.EmailField(max_length=50)
    job_seeker_email = models.EmailField(max_length=50)
    def __str__(self):
        return self.job_seeker_email + ' ' +self.job_title + ' ' + self.job_company_email 
        