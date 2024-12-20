from django.views.generic import ListView, DetailView
from .models import JobListing

class JobList(ListView):
    model = JobListing
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'

class JobDetail(DetailView):
    model = JobListing
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'
