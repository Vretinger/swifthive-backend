from django.contrib import admin
from .models import CustomUser, FreelancerProfile

admin.site.register(CustomUser)
admin.site.register(FreelancerProfile)
