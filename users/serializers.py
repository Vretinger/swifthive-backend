from rest_framework import serializers
from .models import CustomUser, FreelancerProfile


class FreelancerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerProfile
        fields = ['skills', 'hourly_rate', 'portfolio_url', 'profile_image']


class UserSerializer(serializers.ModelSerializer):
    freelancer_profile = FreelancerProfileSerializer()
    projects_count = serializers.IntegerField(read_only=True)
    clients_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'is_freelancer',
            'is_client',
            'freelancer_profile',
            'projects_count',
            'clients_count',
            'date_joined',
        ]
