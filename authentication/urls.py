from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('regiser/', views.UserRegistration.as_view(),name='register'),
]
