from django.urls import path
from . import views

urlpatterns = [
    path('user_messages/', views.UserMessageList.as_view(), name='user-message-list'),
    path('user_messages/<int:pk>/', views.UserMessageDetail.as_view(), name='user-message-detail'),
]
