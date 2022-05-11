from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    path('post-job.html',views.postjob,name='postjob'),
    
    path('login.html',views.login,name='login'),
    
    path('register_user',views.register,name='register'),
    
    path('login_jobseeker.html',views.login_jobseeker,name='login_jobseeker'),
    
    path('login_jobseeker',views.login_eval_jobseeker,name='login_eval_jobseeker'),
    
    path('loggedin_seeker',views.reg_jobseeker,name='jobseeker'),
    
    path('login_jobrecruiter',views.login_eval_jobrecruiter,name='login_jobrecruiter'),
    
    path('login_recruiter',views.login_eval_jobrecruiter,name='login_eval_jobrecruiter'),
    
    path('loggedin_recruiter',views.reg_jobrecruiter,name='jobrecruiter'),
    
    path('job_apply',views.job_apply, name='job_apply'),
    
    path('log',views.login_eval_jobseeker, name='seeker'),
    
    path('post-job.html',views.post_job,name='post_job'),
    
    path('job-single.html',views.job_single,name='job_single'),
    
]