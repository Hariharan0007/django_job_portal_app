from django.shortcuts import render

from rest_framework.decorators import api_view
from .models import jobseeker_model,jobrecruiter_model,jobs_model,job_apply_model
from .serializers import log_jobseeker_Serializer,log_jobrecruiter_Serializer,log_jobsmodel_Serializer,job_apply_Serializer


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
  
		job_models=jobs_model.objects.all()
		serializer_job = log_jobsmodel_Serializer(job_models,many=True)
		jobs_list=[]
		for i in serializer_job.data:
			jobs_list.append(dict(i))
		print(jobs_list)



		#getting a list of jobs which are applied by the seeker  
		job_apply_models=job_apply_model.objects.all()
		serializer_applied_job = job_apply_Serializer(job_apply_models,many=True)
		applied_list=[]
		for i in serializer_applied_job.data:
			applied_list.append(dict(i))
		print("APPLIED JOBS---->>>>",applied_list)
		
    
  
		jobseeker_models=jobseeker_model.objects.all()
		serializer = log_jobseeker_Serializer(jobseeker_models,many=True)
		seekers_list=[]
		for i in serializer.data:
			seekers_list.append(dict(i))
		print("SEEKERS LIST ---->> \n \n",seekers_list)
		Flag=False
		login_seeker=[]
  
  
  
		for attributes in seekers_list:
			Flag=False
			print(attributes)
			if attributes['email']==email and attributes['name']==seeker_name and attributes['pwsd']==pwsd:
				print("INSIDE IF :)")
				login_seeker.append(attributes)
				print("LOGGED IN SEEKER---->> \n \n",login_seeker[0])
				Flag=True
				applied_job_list=[]
				if applied_list!=[]:
					for seeker_job in login_seeker:
						print("SEEKER JOB--> \n \n",seeker_job)
						for app_job in applied_list:
							print("APPLIED JOB -->> \n \n",app_job)
							for jobs in jobs_list:
								print("JOBS---->>> \n \n",jobs)
								print("CONDITION CHECK===>\n \n",app_job['job_title'],app_job['job_company_email'],app_job['job_seeker_email'])
								print("CONDITION CHECK===>\n \n",jobs['job_title'],jobs['job_company_email'],seeker_job['email'])
								if app_job['job_title']==jobs['job_title'] and app_job['job_company_email'] == jobs['job_company_email'] and app_job['job_seeker_email']==seeker_job['email']:
									applied_job_list.append(jobs)
					print("APPLIED JOBS LIST ==>>>",applied_job_list)
					new_jobs_list=[]
					for jb in applied_job_list:
						print(jb)
						for jobs in jobs_list:
							print(jobs)
							if jb['job_title']==jobs['job_title'] and jb['job_company_email']==jobs['job_company_email']:
								pass
							else:
								new_jobs_list.append(jobs)
					print("NEW JOBS LIST",new_jobs_list)
				else:
					new_jobs_list=jobs_list
					applied_job_list=None
				return render(request,'login_jobseeker.html',{'user':login_seeker[0],'jobs':new_jobs_list,'applied_job':applied_job_list})
			print("AFTER IF STATEMENT :(")
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
			applied_job=0,
			applied_company=0
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
 
 
def job_apply(request):
    print("JOB  IS  TRYING  TO APPLY")
    if request.method == 'POST':
        job_name=request.POST.get('job_name')
        job_seeker_mail=request.POST.get('jobseeker_mail_id')
        company_mail=request.POST.get('job_company_email')
        
        print(company_mail)
        print(job_name)
        print(job_seeker_mail)
        
        job_apply = job_apply_model(
			job_seeker_email=job_seeker_mail,
			job_title=job_name,
			job_company_email=company_mail
		)
        
        job_apply.save()
        print("Data Saved in a Model")

        
        # getting a list of jobs  
        job_models=jobs_model.objects.all()
        serializer_job = log_jobsmodel_Serializer(job_models,many=True)
        jobs_list=[]
        for i in serializer_job.data:
            jobs_list.append(dict(i))
        print(jobs_list)
        
        #getting a list of jobs which are applied by the seeker  
        job_apply_models=job_apply_model.objects.all()
        serializer_applied_job = job_apply_Serializer(job_apply_models,many=True)
        applied_list=[]
        for i in serializer_applied_job.data:
            applied_list.append(dict(i))
        print(applied_list)
        
        
        
        #getting data of a seeker 
        jobseeker_models=jobseeker_model.objects.all()
        serializer = log_jobseeker_Serializer(jobseeker_models,many=True)
        seekers_list=[]
        for i in serializer.data:
            seekers_list.append(dict(i))
        print(seekers_list)
        Flag=False
        login_seeker=[]
        
        #getting active job seeker(logged in)
        for attributes in seekers_list:
            Flag=False
            if attributes['email']==job_seeker_mail :
                login_seeker.append(attributes)
                print(login_seeker[0])
                Flag=True
        
        
        #getting applied jobs    
        applied_job_list=[]
        for seeker_job in login_seeker:
            for app_job in applied_list:
                for jobs in jobs_list:
                    if app_job['job_title']==jobs['job_title'] and app_job['job_company_email'] == jobs['job_company_email'] and app_job['job_seeker_email']==seeker_job['email']:
                        applied_job_list.append(dict(jobs))
                        
        
        #update new jobs list
        new_jobs_list=[]
        for jobs in jobs_list:
            for jb in applied_job_list: 
                flag=True
                print("CONDITION CHECK jb===>",jb['job_title'],jb['job_company_email'])
                print("CONDITION CHECK jobs===>",jobs['job_title'],jobs['job_company_email'])
                if jb['job_title']==jobs['job_title'] and jb['job_company_email']==jobs['job_company_email']:
                    flag=False
                if flag!=False:
                    print("JOB ADDED")
                    new_jobs_list.append(jobs)
        print(new_jobs_list)
        
        
        #new_jobs_list=list(set(jobs_list).intersection(set(applied_job_list)))
        #new_jobs_list=[]
        
        
                
            
        

        
        return render(request,'login_jobseeker.html',{'user':login_seeker[0],'jobs':new_jobs_list,'applied_job':applied_job_list})
        #if Flag==False:
        #    return render(request,'register.html')
        
 
 
 
 

def post_job(request):
	return render(request,'post-job.html',{})

def job_single(request):
	return render(request,'job-single.html',{})