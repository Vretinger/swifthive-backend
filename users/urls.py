from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, FreelancerProfileViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'freelancer_profiles', FreelancerProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
