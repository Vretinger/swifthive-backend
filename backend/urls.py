from django.contrib import admin
from django.urls import path, include
from .views import home, logout_route

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),

    path('', include('users.urls')),          # Users
    path('', include('contracts.urls')),      # Contracts
    path('', include('user_messages.urls')),  # User Messages
    path('', include('jobs.urls')),
]

    