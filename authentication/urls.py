from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('regiser/', views.UserRegistration.as_view(),name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(),name='register'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
]