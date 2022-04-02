from ast import Pass
from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm
# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    paginator  = Paginator(jobs,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context= {
        'jobs':page_obj,
    }
    return render(request,'job/job.html',context)
def job_detail(request,slug):

    job_detail = Job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form  = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            form  = ApplyForm()
    else:
        form  = ApplyForm()

    context= {
        'job':job_detail,
        'form':form,
    }
    return render(request,'job/job_detail.html',context)