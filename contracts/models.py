from django.db import models
from users.models import CustomUser
from jobs.models import JobListing

class Contract(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contracts_as_client')
    freelancer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contracts_as_freelancer')
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    agreed_price = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='active')

    def __str__(self):
        return f"Contract between {self.client.username} and {self.freelancer.username} for {self.job.title}"
