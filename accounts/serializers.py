from rest_framework import serializers
from .models import CustomUser , FarmerProfile , BuyerProfile
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required = True , write_only=True,validators = [validate_password])
    password2 = serializers.CharField(required = True ,write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username' , 'email' , 'password' ,'password2', 'phone' , 'role' , 'district']
        extra_kwargs = {
            'phone' : {'required':True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                'password' : 'Password did not match'
            })
        return attrs 
        
    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            #  authenticate with username
            user = authenticate(username=username, password=password)
            
            # If not found, try with email
            if not user:
                try:
                    user_obj = CustomUser.objects.get(email=username)
                    user = authenticate(username=user_obj.username, password=password)
                except CustomUser.DoesNotExist:
                    pass
            
            # Check authentication result
            if not user:
                raise serializers.ValidationError("Invalid credentials")
        
            if not user.is_active:
                raise serializers.ValidationError("Account is disabled")
        else:
            raise serializers.ValidationError({
                'error': 'Must include "username" and "password".'
            })

        attrs['user'] = user
        return attrs

class FarmerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        username = serializers.CharField(source='user.username',read_only=True) #source as they are not in Farmer model
        phone = serializers.CharField(source='user.phone',read_only=True)
        email = serializers.CharField(source='user.email',read_only=True)
        district = serializers.CharField(source='user.district',read_only=True)

        model = FarmerProfile
        fields = ['id' ,'username' , 'phone' , 'email' ,'district', 'farm_name' , 'farm_description' , 'is_verified']
        read_only_fields = [
            'id',
            'is_verified'
        ]

class BuyerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        username = serializers.CharField(source='user.username',read_only=True) #source as they are not in Farmer model
        phone = serializers.CharField(source='user.phone',read_only=True)
        email = serializers.CharField(source='user.email',read_only=True)
        district = serializers.CharField(source='user.district',read_only=True)

        model = BuyerProfile
        fields = ['id' , 'username' , 'phone' , 'email' ,'district','address' , 'business_name' , 'business_type']  
        read_only_field = [
            'id'
        ]      