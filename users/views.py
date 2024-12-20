from rest_framework import viewsets
from .models import CustomUser, FreelancerProfile
from .serializers import CustomUserSerializer, FreelancerProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class FreelancerProfileViewSet(viewsets.ModelViewSet):
    queryset = FreelancerProfile.objects.all()
    serializer_class = FreelancerProfileSerializer

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]