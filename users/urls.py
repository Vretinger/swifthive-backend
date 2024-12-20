from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, FreelancerProfileViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router for the viewsets
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'freelancer-profiles', FreelancerProfileViewSet)

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Includes the viewsets from the router
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
