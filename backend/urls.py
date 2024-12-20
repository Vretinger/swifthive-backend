from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),          # Users
    path('', include('contracts.urls')),      # Contracts
    path('', include('user_messages.urls')),  # User Messages
    path('', include('jobs.urls')),
]