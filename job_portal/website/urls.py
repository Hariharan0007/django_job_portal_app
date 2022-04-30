from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    path('post-job.html',views.postjob,name='postjob'),
    
    path('login.html',views.login,name='login'),
    
    path('register.html',views.register,name='register'),
    
    path('login_jobseeker.html',views.login_jobseeker,name='login_jobseeker'),
    
    path('login_jobseeker',views.login_eval_jobseeker,name='login_eval_jobseeker'),
    
    path('loggedin',views.reg_jobseeker,name='jobseeker'),
    
    path('login_jobrecruiter.html',views.login_jobrecruiter,name='login_jobrecruiter'),
    
    path('login_jobrecruiter',views.login_eval_jobrecruiter,name='login_eval_jobrecruiter'),
    
    path('loggedin',views.reg_jobrecruiter,name='jobrecruiter'),
    
    path('post-job.html',views.post_job,name='post_job'),
    
    path('job-single.html',views.job_single,name='job_single'),
    
]