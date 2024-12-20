from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_freelancer = models.BooleanField(default=False)  # To distinguish freelancers from clients
    is_client = models.BooleanField(default=False)      # To distinguish clients from freelancers


class FreelancerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='freelancer_profile')
    skills = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    portfolio_url = models.URLField()

    def __str__(self):
        return f"{self.user.username}'s Profile"