from django.urls import path
from . import views

urlpatterns = [
    path('contracts/', views.ContractList.as_view(), name='contract-list'),
    path('contracts/<int:pk>/', views.ContractDetail.as_view(), name='contract-detail'),
]
