from django.contrib.auth.models import AbstractUser
from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api

class CustomUser(AbstractUser):
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

class FreelancerProfile(models.Model):
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, related_name='freelancer_profile')
    skills = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    portfolio_url = models.URLField()
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
