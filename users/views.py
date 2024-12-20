from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.permissions import IsOwnerOrReadOnly
from .models import CustomUser
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    """
    List all users with aggregated information for freelancers and clients.
    """
    queryset = CustomUser.objects.annotate(
        projects_count=Count('freelancer_profile__projects', distinct=True),  # Assuming a related_name 'projects' on FreelancerProfile
        clients_count=Count('freelancer_profile__clients', distinct=True)     # Assuming a related_name 'clients' on FreelancerProfile
    ).order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'freelancer_profile__skills',  # Filter by specific skills
        'is_freelancer',               # Filter by freelancer status
        'is_client',                   # Filter by client status
    ]
    ordering_fields = [
        'projects_count',
        'clients_count',
        'date_joined',
    ]


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update user details if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = CustomUser.objects.annotate(
        projects_count=Count('freelancer_profile__projects', distinct=True),
        clients_count=Count('freelancer_profile__clients', distinct=True)
    ).order_by('-date_joined')
    serializer_class = UserSerializer
