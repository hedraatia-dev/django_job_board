from django.shortcuts import render

# Create your views here.
#from .models import Job
from .models import Job, Category

def job_list(request):
    job_list = Job.objects.all()
    context ={'jobs' : job_list}  # template name
    return render(request,'job/job_list.html', context)




def job_detail(request, id):
    job_detail = Job.objects.get(id=id)
    context ={'job' : job_detail}  # template name
    return render(request,'job/job_detail.html', context)
