from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('contracts/', include('contracts.urls')),
    path('jobs/', include('jobs.urls')),
    path('user_messages/', include('user_messages.urls')),
]