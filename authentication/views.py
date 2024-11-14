from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from . models import User
from rest_framework import status
from . serializer import UserRegisterSerializer,MyTokenObtainPairSerializer

# Create your views here.


class UserRegistration(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username = serializer.validated_data['username'],
                first_name = serializer.validated_data['first_name'],
                last_name = serializer.validated_data['last_name'],
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password'],
            )
            return Response({"message":"Registration Successfully completed"},status=status.HTTP_201_CREATED)
        return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer