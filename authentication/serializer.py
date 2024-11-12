from rest_framework import serializers
from . models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','password2']


    def validate(self,data):
        password = data.get('password')
        password2 = data.get('password2')

        # length = len(password)

        # if length<8:
        #     raise serializers.ValidationError({'password8':'Password must need 8 charecters'})
            
        # if password != password2:
        #     raise serializers.ValidationError({'password_error':'password doesnt match'})
            
            
        return data