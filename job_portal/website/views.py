from django.shortcuts import render

from rest_framework.decorators import api_view
from .models import jobseeker_model,jobrecruiter_model,jobs_model
from .serializers import log_jobseeker_Serializer,log_jobrecruiter_Serializer,log_jobsmodel_Serializer


# Create your views here.

def home(request):
	return render(request,'login.html',{})

def postjob(request):
	return render(request,'post-job.html',{})

def login(request):
	return render(request,'login.html',{})

@api_view(['GET','POST'])
def login_eval_jobrecruiter(request):
	if request.method == 'POST':
		rec_name=request.POST.get('name')
		email=request.POST.get('email')
		pwsd=request.POST.get('password')
		print(rec_name,email,pwsd)
  
  
		try:
			job_title=request.POST.get('job-title')
			job_desc=request.POST.get('job-desc')
			job_skills=request.POST.get('job-skills')
			job_experience=request.POST.get('job-experiance')
			job_company_name=request.POST.get('company-name')
			job_company_email=request.POST.get('company-email')

			print(job_title,job_experience)

  
			print("Inside request.post")
			reg = jobs_model(
				job_title=job_title,
				job_description=job_desc,
				job_skills=job_skills,
				job_experiance=job_experience,
				job_company_name=job_company_name,
				job_company_email=job_company_email,
				)
			if job_title!=None:
				reg.save()
			print(reg)
		except:
			pass

		job_models=jobs_model.objects.all()
		serializer_job = log_jobsmodel_Serializer(job_models,many=True)
		jobs_list=[]
		for i in serializer_job.data:
			jobs_list.append(dict(i))
		print(jobs_list)
  



		jobrecruiter_models=jobrecruiter_model.objects.all()
		serializer = log_jobrecruiter_Serializer(jobrecruiter_models,many=True)
		recruiter_list=[]
		for i in serializer.data:
			recruiter_list.append(dict(i))
		print(recruiter_list)
  
		if rec_name==None:
			for attributes in recruiter_list:
				if attributes['company_name']==job_company_name:
					rec_name=attributes['name']
					email=attributes['email']
					pwsd= attributes['pwsd']
					break
  
  
		Flag=False
		login_recruiter=[]
  

		company_job_list=[]
		for attributes in recruiter_list:
			Flag=False
			if attributes['email']==email and attributes['name']==rec_name and attributes['pwsd']==pwsd:
				login_recruiter.append(attributes)
				print(login_recruiter[0])
				recruiter=login_recruiter[0]
				Flag=True
				print(jobs_list)
				for job in jobs_list:
					print(job['job_company_name'])
					print(recruiter['company_name'])
					if job['job_company_name']==recruiter['company_name']:
						print("JOB IS ADDED TO FILE LIST")
						company_job_list.append(job)
				print(company_job_list)
				return render(request,'login_jobrecruiter.html',{'user':login_recruiter[0],'jobs':company_job_list})
			if Flag==True:
				break
				
		if Flag==False:
			return render(request,'register.html')

 
def login_eval_jobseeker(request):
	if request.method == 'POST':
		seeker_name=request.POST.get('name')
		email=request.POST.get('email')
		pwsd=request.POST.get('password')
		print(seeker_name,email,pwsd)
		jobseeker_models=jobseeker_model.objects.all()
		serializer = log_jobseeker_Serializer(jobseeker_models,many=True)
		seekers_list=[]
		for i in serializer.data:
			seekers_list.append(dict(i))
		print(seekers_list)
		Flag=False
		login_seeker=[]
		for attributes in seekers_list:
			Flag=False
			if attributes['email']==email and attributes['name']==seeker_name and attributes['pwsd']==pwsd:
				login_seeker.append(attributes)
				print(login_seeker[0])
				Flag=True
				return render(request,'login_jobseeker.html',{'user':login_seeker[0]})
			if Flag==True:
				break
				
		if Flag==False:
			return render(request,'register.html') 


def register(request):
	return render(request,'register.html',{})

@api_view(['GET','POST'])

def reg_jobseeker(request):
    if request.method == 'POST':
        print("Inside request.post")
        seeker_name=request.POST.get('name')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        repwsd=request.POST.get('repwsd')
        degree=request.POST.get('degree')
        poy=request.POST.get('poy')
        percentile=request.POST.get('percentile')
        experiance=request.POST.get('experiance')
        
        print(seeker_name,email,dob,mobile,password,degree,poy,experiance)
        
        reg = jobseeker_model(
			name=seeker_name,
			email=email,
			dob=dob,
			mobile=mobile,
			pwsd=password,
			repwsd=repwsd,
			degree=degree,
			passed_out_year=poy,
			percentile=percentile,
			experience=experiance,
			applied_job="None",
			applied_company="None"
   		)
        reg.save()
        print(reg)
        return render(request,'login_jobseeker.html',{'user':reg})
        #return render("about.html")
        
        
        

def login_jobseeker(request):
	return render(request,'login_jobseeker.html',{})



@api_view(['GET','POST'])

def reg_jobrecruiter(request):
	if request.method == 'POST':
		print("######################## REGISTERING JOB RECRUITER ########################")
		print("Inside Request.post")
		rec_name=request.POST.get('name')
		email=request.POST.get('email')
		mobile=request.POST.get('mobile')
		password=request.POST.get('password')
		repwsd=request.POST.get('re_type_pwsd')
		com_name=request.POST.get('company_name')
		com_desc=request.POST.get('company_desc')

		reg_recruiter = jobrecruiter_model(
			name=rec_name,
			email=email,
			mobile=mobile,
			pwsd=password,
			repwsd=repwsd,
			company_name=com_name,
			company_desc=com_desc,
		)

		reg_recruiter.save()
		print(reg_recruiter)

		return render(request,'login.html',{'user':reg_recruiter})

"""
def login_jobrecruiter(request):
	return render(request,'login_jobrecruiter.html',{})
	"""
 
 
 
 

def post_job(request):
	return render(request,'post-job.html',{})

def job_single(request):
	return render(request,'job-single.html',{})