from django.contrib.auth.models import AbstractUser
from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Custom User model
class CustomUser(AbstractUser):  # Inherit from AbstractUser to include default user fields
    freelancer_profile = models.OneToOneField(
        'FreelancerProfile', on_delete=models.CASCADE, related_name='user_profile', null=True, blank=True
    )
    is_freelancer = models.BooleanField(default=False)  # To distinguish freelancers from clients
    is_client = models.BooleanField(default=False)      # To distinguish clients from freelancers

    # Add custom related names to avoid clashes with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related name for groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Custom related name for user_permissions
        blank=True
    )

    def __str__(self):
        return self.username  # Return username as a string representation of the user


# Freelancer Profile model
class FreelancerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile_user')
    projects = models.ManyToManyField('Project', related_name='freelancer_profiles')
    clients = models.ManyToManyField('Client', related_name='freelancer_profiles')
    skills = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    portfolio_url = models.URLField()
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# Project model (example, you can adjust this to your needs)
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


# Client model (example, you can adjust this to your needs)
class Client(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
